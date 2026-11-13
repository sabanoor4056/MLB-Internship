# Day 28 - Computer Vision Image Processing Studio

## Project Overview

Computer Vision Image Processing Studio is a simple web application built using Python, OpenCV, NumPy, and Streamlit.

It allows users to upload an image, select different image processing operations, view the processed image, and download the result through a web-based interface.

## Features

The application includes the following image processing operations:

1. **Grayscale** - Converts an image into black and white.
2. **Blur** - Makes the image smooth.
3. **Edge Detection** - Detects edges and boundaries.
4. **Image Rotation** - Rotates the image 90 degrees clockwise.
5. **Image Enhancement** - Improves image quality using CLAHE.
6. **Contour Detection** - Detects and draws object outlines.
7. **Brightness Adjustment** - Adjusts image brightness using a slider (Custom Challenge Feature).

## Technologies Used

- Python
- OpenCV
- NumPy
- Streamlit

## Project Structure

```text
Day28/
│
├── app.py
├── practice.py
├── requirements.txt
├── README.md
│
├── input_images/
│   └── sample.jpg
│
└── output_images/
    └── processed_image.png
```

## Installation

### Step 1: Install Required Libraries

Open your terminal and run:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

Run the following command in your terminal:

```bash
python -m streamlit run app.py
```

### Step 3: Open the Application

After running the command, Streamlit will provide a local URL in the terminal.

Open this link in your browser:

http://localhost:8501

## How to Use

1. Open the application in your browser.
2. Upload an image.
3. Select an image processing operation.
4. Adjust brightness if needed.
5. Click the **Process Image** button.
6. View the original and processed images.
7. Download the processed image.

## Custom Challenge Feature

Brightness Adjustment is the additional custom feature.

It allows users to increase or decrease image brightness using a slider.

## Learning Outcomes

- Learned how to organize a Computer Vision project.
- Learned to create reusable Python functions.
- Practiced different OpenCV image processing techniques.
- Learned to build a web interface using Streamlit.
- Learned how to save and download processed images.
- Learned how to run a local web application using Streamlit.

