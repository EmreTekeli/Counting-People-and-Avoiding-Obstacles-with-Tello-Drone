from djitellopy import Tello
import cv2
import numpy as np
import math
import time

tello = Tello()
tello.connect()
tello.streamon()

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

classes = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light",
           "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow"]

kp = 0.1 
ki = 0.01
kd = 0.05

target_distance = 100
target_angle = 0


prev_error = 0
integral = 0

tello.takeoff()

x = 0
y = 0
w = 0
h = 0

in_air = True
drone_360_turn = False
turn_duration = 500
turn_start_time = 0

while True:
    try:
        frame = tello.get_frame_read().frame

        height, width, channels = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        obstacle_positions = []

        human_count = 0
        for i in range(len(boxes)):
            if i in indexes and i < len(class_ids):
                label = str(classes[class_ids[i]])
                if label == "person":
                    human_count += 1
                confidence = confidences[i]
                color = (0, 255, 0)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                obstacle_positions.append((x + w // 2, y + h // 2))

        cv2.putText(frame, f'Human Count: {human_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if not drone_360_turn and human_count > 0:
            drone_360_turn = True
            tello.send_rc_control(0, 0, 0, 30)
            turn_start_time = time.time()
        elif drone_360_turn and human_count == 0:
            if time.time() - turn_start_time >= turn_duration:
                drone_360_turn = False
                tello.send_rc_control(0, 0, 0, 0)

        if obstacle_positions:
            obstacle_x, obstacle_y = obstacle_positions[0]

            obstacle_distance = math.sqrt((obstacle_x - width / 2) ** 2 + (obstacle_y - height / 2) ** 2)
            error = target_distance - obstacle_distance
            integral += error
            derivative = error - prev_error
            speed = kp * error + ki * integral + kd * derivative

            max_speed = 50
            min_speed = -50
            speed = max(min(speed, max_speed), min_speed)

            tello.send_rc_control(0, 0, int(speed), 0)

            prev_error = error

        cv2.imshow('Tello Insan sayim', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        if key == ord('l'):
            tello.land()
            in_air = False

    except Exception as e:
        print(f'Hata oluştu: {e}')

cv2.destroyAllWindows()
