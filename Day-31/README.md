
# Day 31 – Road Damage Detection Using YOLO11n

## Project Overview
This project detects road damage using a custom-trained YOLO11n object detection model. The dataset was selected from Roboflow Universe and contains seven road damage categories.

## Dataset
The dataset was downloaded in YOLO format.

- Training images: 5,994
- Validation images: 1,797
- Testing images: 795
- Total classes: 7

### Classes
1. Alligator Cracks
2. Damaged crosswalk
3. Damaged paint
4. Longitudinal Cracks
5. Manhole cover
6. Potholes
7. Transverse Cracks

The dataset was selected to train a model capable of detecting multiple types of road damage.

## Model and Training Configuration

- Model: YOLO11n
- Framework: Ultralytics
- Epochs: 20
- Batch size: 8
- Image size: 640 × 640
- Device: NVIDIA Tesla T4 GPU
- Platform: Google Colab

## Final Test Evaluation

| Metric | Score |
|---|---:|
| Precision | 59.52% |
| Recall | 54.20% |
| mAP@50 | 56.83% |
| mAP@50-95 | 29.93% |

The target mAP@50 was 80%. The achieved score was 56.83%, so the target was not reached.

## Class-wise Test mAP@50

| Class | Score |
|---|---:|
| Alligator Cracks | 61.7% |
| Damaged crosswalk | 77.5% |
| Damaged paint | 56.3% |
| Longitudinal Cracks | 34.0% |
| Manhole cover | 85.6% |
| Potholes | 50.0% |
| Transverse Cracks | 32.8% |

## Challenges and Observations

- The dataset YAML paths initially needed correction.
- Some road damage categories, especially crack classes, were harder to detect.
- Image access from mounted storage was slower than local storage.
- The model performed better on manhole covers and damaged crosswalks.
- Further experiments with epochs, batch size, image size, and augmentation are needed to improve performance.

## Application

The Streamlit application allows users to:
- Upload road images and videos.
- Detect road damage using the trained YOLO11n model.
- View detected categories and confidence scores.
- Download processed images and videos.

## Project Files

- `app.py`: Streamlit application
- `weights/best.pt`: Trained model
- `requirements.txt`: Python dependencies
- `training_notebook.ipynb`: Training notebook
- `sample_test_images/`: Original test images
- `prediction_results/`: Annotated predictions
- `README.md`: Project documentation
