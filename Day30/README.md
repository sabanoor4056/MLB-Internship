
# Day 30 - Image Segmentation

## Introduction
Image segmentation is a computer vision technique
used to divide an image into different regions.
It helps separate the main object from the background.

## Techniques Implemented

### 1. Binary Thresholding
Uses a fixed threshold value to convert an image
into black and white pixels.

### 2. Adaptive Thresholding
Calculates different threshold values for different
small regions of an image. It is useful for uneven
lighting and shadows.

### 3. Otsu Thresholding
Automatically calculates a suitable threshold value
to separate foreground and background.

### 4. Foreground Segmentation
Uses a binary mask to keep the main object and
remove the background.

## Dataset
Used at least 15 images, including:
- Documents
- Objects on plain backgrounds
- Images with uneven lighting
- Images containing shadows

## Best Performing Method
Adaptive Thresholding worked better for many of my
document images because it handles uneven lighting.

Otsu Thresholding worked well for images with clear
foreground and background contrast.

The best method depends on the image.

## Challenges
- Handling uneven lighting.
- Removing shadows.
- Separating objects from complex backgrounds.
- Selecting the appropriate thresholding method.

## Technologies Used
- Python
- OpenCV
- NumPy
- Streamlit

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Project Features
- Upload an image.
- Select segmentation methods.
- View processed results.
- Download segmented images.

