# eagleview
eagleview
YOLO – YOU ONLY LOOK ONCE YOLO came on the computer vision scene with a paper released in 2015 by Joseph Redmon et al. “You Only Look Once: Unified, Real-Time Object Detection,”
and immediately got a lot of attention from fellow computer vision researchers. Convolutional Neural Networks (CNN) such as RegionConvolutional Network (R-CNN) used Regions 
Proposal Networks (RPNs) before YOLO was invented, it produces proposal bounding boxes on the input image first, then runs a classifier on the bounding boxes and then apply 
post-processing to remove duplicate detections and refine the bounding boxes. It was not suitable for training individual stages of the R-CNN network separately. The R-CNN 
network was both difficult and sluggish to optimize. The author's motivation is to build a unified model of all phases on a neural network. With the input image containing 
(or not) the objects, after passing forward through a single neural network of multiple convolutional networks, the system produces predictive vectors corresponding to each 
object appearing in the image. Instead of iterating the process of classifying different regions on the image, the YOLO system computes all the features of the image and makes 
predictions for all objects at the same time. That is the idea of "You Only Look Once". (Redmon, et al., 2016)

Overview of YOLOv5 Besides, Glenn Jocher is also the inventor of the Mosaic data augmentation and acknowledged by Alexey Bochkovsky in the YOLOv4 paper (Bochkovskiy, et al., 2020).
However, his YOLOv5 model caused lots of controversy in the computer vision community because of its name and improvements. Despite being released a month after YOLOv4, the start 
of research for YOLOv4 and YOLOv5 was quite close (March – April 2020). For avoiding collision, Glenn decided to name his version of YOLO, YOLOv5. Thus, basically, both researchers
applied the state-of-the-art innovations in the field of computer vision at that time. That makes the architecture of YOLOv4 and YOLOv5 very similar and it makes many people 
dissatisfied with the name YOLOv5 (5th generation of YOLO) when it does not contain multiple outstanding improvements compared to the previous version YOLOv4. Besides, Glenn 
did not publish any paper for YOLOv5, causing more suspicions about YOLOv5. However, YOLOv5 possessed the advantages in engineering. YOLOv5 is written in Python programming 
language instead of C as in previous versions. That makes installation and integration on IoT devices easier. In addition, the PyTorch community is also larger than the Darknet 
community, which means that PyTorch will receive more contributions and growth potential in the future. Due to being written in 2 different languages on 2 different frameworks, 
comparing the performance between YOLOv4 and YOLOv5 is difficult to be accurate. But after a while, YOLOv5 37 has proved higher performance than YOLOv4 under certain circumstances
and partly gained confidence in the computer vision community besides YOLOv4. 4.2 Notable differences – Adaptive anchor boxes As mentioned above, the YOLOv5 architecture has 
integrated the latest innovations similar to the YOLOv4 architecture, thus there are not many brilliant differences in theory. The author did not publish a detailed paper, but 
only launched a repository on Github and updates improvements there. By dissecting its structure code in file .yaml, the YOLOv5 model can be summarized as follows 
(Jocher, 2020):

Backbone: Focus structure, CSP network - Neck: SPP block, PANet - Head: YOLOv3 head using GIoU-loss The remarkable point mentioned by the YOLOv5 author is an engineering difference. Joseph Redmon introduced the anchor box structure in YOLOv2 and a procedure for selecting anchor boxes of size and shape that closely resemble the ground truth bounding boxes in the training set. By using the k-mean clustering algorithm with different 𝑘 values, the authors picked the 5 best-fit anchor boxes for the COCO dataset (containing 80 classes) and use them as the default. That reduces training time and increases the accuracy of the network. However, when applying these 5 anchor boxes to a unique dataset (containing a class not belonged to 80 classes in the COCO dataset), these anchor boxes cannot quickly adapt to the ground truth bounding boxes of this unique dataset. For example, a giraffe dataset prefers the anchor boxes with the shape thin and higher than a square box. To address this problem, computer vision engineers usually run the k-mean clustering algorithm on the unique dataset to get the best-fit anchor boxes for the data first. Then, these parameters will be configurated manually in the YOLO architecture. Glenn Jocher proposed integrating the anchor box selection process into YOLOv5. As a result, the network has not to consider any of the datasets to be used as input, it will automatically "learning" the best anchor boxes for that dataset and use them during training. (Solawetz, 2020).
Solution

Convert the json format dataset into yolo format using #links
Split the dataset i.e train/val
Clone the yolov5 repo using #links
Install the requirements
STEPS BEFORE TRAINING DATASET:
Go to yolov5/data/ Open coco128.yaml 
Edit the following inside it: Training and Test file path Number of classes and Class names.

Train it using - !python train.py --img 416 --batch 8 --epochs 10 --data coco128.yaml --weights yolov5s.pt --nosave --cache
