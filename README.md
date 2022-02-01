YOLO v5 Model Architecture
As YOLO v5 is a single-stage object detector, it has three important parts like any other single-stage object detector.

Model Backbone
Model Neck
Model Head
Model Backbone is mainly used to extract important features from the given input image. In YOLO v5 the CSP — Cross Stage Partial Networks are used as a backbone to extract rich in informative features from an input image.

CSPNet has shown significant improvement in processing time with deeper networks. Refer to the following image, for more information about CSPNet visit the Github repo.


Source: https://github.com/WongKinYiu/CrossStagePartialNetworks/blob/master/fig/cmp3.png
Model Neck is mainly used to generate feature pyramids. Feature pyramids help models to generalized well on object scaling. It helps to identify the same object with different sizes and scales.

Feature pyramids are very useful and help models to perform well on unseen data. There are other models that use different types of feature pyramid techniques like FPN, BiFPN, PANet, etc.

In YOLO v5 PANet is used for as neck to get feature pyramids. For more information on features pyramids, refer to the following link.

Understanding Feature Pyramid Networks for object detection (FPN)

The model Head is mainly used to perform the final detection part. It applied anchor boxes on features and generates final output vectors with class probabilities, objectness scores, and bounding boxes.

In YOLO v5 model head is the same as the previous YOLO V3 and V4 versions.

Additionally, I am attaching the final model architecture for YOLO v5 — a small version.

Activation Function
The choice of activation functions is most crucial in any deep neural network. Recently lots of activation functions have been introduced like Leaky ReLU, mish, swish, etc.

YOLO v5 authors decided to go with the Leaky ReLU and Sigmoid activation function.

In YOLO v5 the Leaky ReLU activation function is used in middle/hidden layers and the sigmoid activation function is used in the final detection layer. You can verify it here.

Optimization Function
For optimization function in YOLO v5, we have two options

SGD
Adam
In YOLO v5, the default optimization function for training is SGD.

However, you can change it to Adam by using the “ — — adam” command-line argument.

Cost Function or Loss Function
In the YOLO family, there is a compound loss is calculated based on objectness score, class probability score, and bounding box regression score.

Ultralytics have used Binary Cross-Entropy with Logits Loss function from PyTorch for loss calculation of class probability and object score.

We also have an option to choose the Focal Loss function to calculate the loss. You can choose to train with Focal Loss by using fl_gamma hyper-parameter
Solution

Convert the json format dataset into yolo format using #links
Split the dataset i.e train/val
Clone the yolov5 repo using #links
Install the requirements
STEPS BEFORE TRAINING DATASET:
Go to yolov5/data/ Open coco128.yaml 
Edit the following inside it: Training and Test file path Number of classes and Class names.

Train it using - !python train.py --img 416 --batch 8 --epochs 10 --data coco128.yaml --weights yolov5s.pt --nosave --cache


METRICS
       Class     Images     Labels    Precision  Recall     mAP@.5 mAP@.5:.95: 100% 5/5 [00:04<00:00,  1.17it/s]
         all        144        975      0.283      0.233      0.193     0.0755
         person     144        596      0.219      0.178      0.121      0.035
         car        144        379      0.347      0.288      0.265      0.116
            
  RECOMMENDATION
  
1. To achieve a good accuracy, we need a dataset >2-3k images
2. Good accuracy can also be achieved on a smaller dataset considering the annotation / labelling of images is correctly done.
3. Tweaking images size can also attain good accuracy 
4. Training it for more than 1000 epochs might also help in achieving good model
