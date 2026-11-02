
# Day 22 - Transfer Learning

## Project Title
Cats vs Dogs Image Classifier using MobileNetV2

## 1. Introduction
Today I learned about Transfer Learning and
pre-trained CNN models using TensorFlow/Keras.

I also created an image classification model
to identify Cats and Dogs.

## 2. What is Transfer Learning?
Transfer Learning is a technique where we use
an already-trained model for a new task.

It saves time, training resources and data.

## 3. Why MobileNetV2?
I selected MobileNetV2 because:

- It is lightweight.
- It requires less computing power.
- It provides good image classification performance.
- It is suitable for mobile and edge devices.

## 4. Dataset
Dataset: Cats vs Dogs

Source: TensorFlow Datasets (TFDS)

Classes:
- Cat
- Dog

Dataset Split:
- 80% Training
- 20% Validation

## 5. Implementation
I performed the following steps:

1. Loaded the Cats vs Dogs dataset.
2. Resized images to 224x224.
3. Preprocessed the images.
4. Loaded pre-trained MobileNetV2.
5. Froze the base model layers.
6. Added custom classification layers.
7. Trained the model.
8. Fine-tuned the last 30 layers.
9. Evaluated the model.
10. Generated accuracy and loss graphs.
11. Displayed sample predictions.

## 6. Experiments
Model: MobileNetV2

Initial Learning Rate: 0.001

Fine-Tuning Learning Rate: 0.00001

Batch Size: 32

Initial Epochs: 8

Fine-Tuning Epochs: 5

Data Augmentation:
- Horizontal Flip
- Random Rotation

## 7. Final Results

Final Validation Accuracy: [Add your actual accuracy]%

Final Validation Loss: [Add your actual loss]

## 8. Challenges
- Loading the dataset.
- Understanding pre-trained models.
- Preprocessing images.
- Training and fine-tuning the model.
- Managing training time and resources.

## 9. What I Learned
- Transfer Learning
- MobileNetV2
- Feature Extraction
- Fine-Tuning
- Image Preprocessing
- Model Training and Evaluation
- Accuracy and Loss Visualization

## 10. Conclusion
Successfully implemented a Cats vs Dogs
Image Classifier using Transfer Learning
and MobileNetV2.
