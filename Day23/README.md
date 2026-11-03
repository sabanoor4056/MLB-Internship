
# Day-23: Object Detection using YOLO

## Introduction

Today I learned about Object Detection and YOLO
(You Only Look Once).

Object Detection is a computer vision technique
that identifies objects in an image and locates
them using bounding boxes.

## Image Classification vs Object Detection

Image Classification identifies the main object
in an image.

Object Detection identifies multiple objects
and shows their locations using bounding boxes.

## What is YOLO?

YOLO stands for You Only Look Once.

It is a popular object detection model used to
detect multiple objects quickly.

It provides:
- Object names
- Bounding boxes
- Confidence scores

## Tools and Technologies

- Python
- VS Code
- Ultralytics YOLOv8
- OpenCV

## Dataset Used

Vehicle Detection Dataset from Roboflow Universe.

Dataset format: YOLOv8

## Practical Work

1. Installed the Ultralytics package.
2. Loaded a pre-trained YOLOv8 model.
3. Performed detection on a single image.
4. Performed detection on multiple images.
5. Tested the model on personal images.
6. Displayed class names and confidence scores.
7. Saved output images with bounding boxes.

## Observations

The model successfully detected common objects
such as cars, people, buses and motorcycles
where visible in the images.

Bounding boxes showed the locations of detected
objects.

Confidence scores helped understand how confident
the model was about each prediction.

Some objects may be missed or incorrectly detected,
especially when objects are small or unclear.

## Training

No model training was performed.

A pre-trained YOLOv8 model was used for inference.

## Conclusion

This practice helped me understand the basic
workflow of object detection using YOLO.

I learned how to load a pre-trained model,
detect objects, interpret bounding boxes,
understand confidence scores and save results.

## Folder Contents

- practice_single.py
- practice_multiple.py
- practice_details.py
- mini_project.py
- input_images/
- dataset/
- output_images/
- requirements.txt
