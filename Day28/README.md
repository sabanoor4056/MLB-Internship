
# Day 28 - Computer Vision Image Processing Studio

## Project Overview
Computer Vision Image Processing Studio is a simple web application built using Python, OpenCV, and Gradio.

It allows users to upload an image, select different image processing operations, view the processed image, and download the result.

## Features

The application includes the following image processing operations:

1. Grayscale - Converts an image into black and white.
2. Blur - Makes the image smooth.
3. Edge Detection - Detects edges and boundaries.
4. Image Rotation - Rotates the image 90 degrees clockwise.
5. Image Enhancement - Improves image quality using CLAHE.
6. Contour Detection - Detects and draws object outlines.
7. Brightness Adjustment - Adjusts image brightness (Custom Challenge Feature).

## Technologies Used

- Python
- OpenCV
- NumPy
- Gradio

## Project Structure

Day28/
│
├── app.py
├── requirements.txt
├── README.md
│
├── input_images/
│   └── sample.jpg
│
└── output_images/
    └── processed_image.png

## Installation

### Step 1: Install Required Libraries

Open your terminal and run:

pip install -r requirements.txt

### Step 2: Run the Application

Run the following command:

python app.py

### Step 3: Open the Application

Open this link in your browser:

http://127.0.0.1:7860

## How to Use

1. Open the application.
2. Upload an image.
3. Select an image processing operation.
4. Adjust brightness if needed.
5. Click the Process Image button.
6. View the original and processed images.
7. Download the processed image.

## Custom Challenge Feature

Brightness Adjustment is the additional custom feature.

It allows users to increase image brightness using a slider.

## Learning Outcomes

- Learned how to organize a Computer Vision project.
- Learned to create reusable Python functions.
- Practiced different OpenCV image processing techniques.
- Learned to build a web interface using Gradio.
- Learned how to save and download processed images.
- Learned the basics of deploying applications using Hugging Face Spaces.

## Project Information

Day: 28

Project: Computer Vision Image Processing Studio

Developer: Saba Noor

## Links

GitHub Repository: Add your GitHub project link here.

Hugging Face Space: Add your deployed application link here.
