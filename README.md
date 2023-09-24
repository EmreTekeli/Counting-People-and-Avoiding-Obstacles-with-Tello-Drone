# Counting People and Avoiding Obstacles with Tello Drone

## Project Description:
This project introduces an application that uses DJI Tello drone to avoid obstacles and count humans in an image. Additionally, it detects objects in the image using the YOLO (You Only Look Once) object detection model. The project also ensures that the drone avoids obstacles using the PID (Proportional-Integral-Derivative) control algorithm.

## Technologies Used:
- DJI Tello Drone: DJI Tello drone is used in this project, and the djitellopy library is used to control the drone.
- YOLO Model: The YOLO (You Only Look Once) model is used for object detection.
- OpenCV: OpenCV is used for image processing and object detection.
- PID Control Algorithm: The PID control algorithm is implemented for obstacle avoidance by the drone.

## Steps to Run the Project:
1. Start your Tello drone and establish a connection.
2. Add the weights and configuration files for the YOLO model to the root directory of your project.
3. Run the project code.
4. The drone will process the image, count humans in it, and avoid obstacles.
5. You can use keyboard shortcuts to control the drone's movement. (You can exit with the "q" key)

## Notes:
- Before running the project, ensure that your drone and DJI Tello API are configured properly.
- Make sure you provide the appropriate weight and configuration files for the YOLO model.

This project provides an example of how DJI Tello drone can be used in various applications. The drone's abilities to perform object detection and avoid obstacles using PID control can serve as a foundational building block for different application scenarios.



## Proje Açıklaması:
Bu proje, DJI Tello drone kullanarak engelden kaçınan ve görüntü üzerindeki insanları sayan bir uygulamayı tanıtır. Ayrıca, YOLO (You Only Look Once) nesne tanıma modelini kullanarak görüntüdeki nesneleri tespit eder. Projede ayrıca PID (Proportional-Integral-Derivative) kontrol algoritması kullanılarak drone'un engellerden kaçınması sağlanır.

## Kullanılan Teknolojiler:
- DJI Tello Drone: Bu projede DJI Tello drone kullanılmıştır. Drone'u kontrol etmek için djitellopy kütüphanesi kullanılmıştır.
- YOLO Modeli: Nesne tanıma işlemi için YOLO (You Only Look Once) modeli kullanılmıştır.
- OpenCV: Görüntü işleme ve nesne tanıma için OpenCV kullanılmıştır.
- PID Kontrol Algoritması: Drone'un engelden kaçınma işlemi için PID kontrol algoritması uygulanmıştır.

## Projeyi Çalıştırma Adımları:
1. Tello drone'unuzu başlatın ve bağlantıyı kurun.
2. YOLO modeli için ağırlıklar ve yapılandırma dosyalarını projenizin kök dizinine ekleyin.
3. Proje kodunu çalıştırın.
4. Drone, görüntüyü işleyecek ve üzerindeki insanları sayacak, ayrıca engellerden kaçınacaktır.
5. Drone'un hareketini kontrol etmek için klavye kısayol tuşlarını kullanabilirsiniz. ("q" tuşu ile çıkış yapabilirsiniz)

## Notlar:
- Projeyi çalıştırmadan önce, drone'unuzun ve DJI Tello API'nin uygun şekilde yapılandırıldığından emin olun.
- YOLO modeli için uygun ağırlık ve yapılandırma dosyalarını sağladığınızdan emin olun.

Bu proje, DJI Tello drone'un çeşitli uygulamalarda kullanılabilmesi için bir örnek sunar. Drone'un nesne tanıma ve PID kontrolü kullanarak engellerden kaçınması ve insan sayma yetenekleri, farklı uygulama senaryoları için temel bir yapı taşını oluşturabilir.
