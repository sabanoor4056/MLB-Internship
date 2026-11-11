# Day 26 – Video Processing with OpenCV

## Project Overview

Today, I learned video processing using Python and OpenCV. I created a video processing application that can read videos, process video frames, detect edges, and save processed videos.

I also created a web application using Streamlit where users can upload a video and see the processed output.

## Topics Covered

- Reading videos using OpenCV
- Capturing video frames
- Understanding FPS (Frames Per Second)
- Getting video properties (width, height, and total frames)
- Writing and saving videos
- Real-time webcam processing
- Grayscale conversion
- Gaussian Blur
- Canny Edge Detection

## Technologies Used

- Python 3.12
- OpenCV
- Streamlit
- NumPy
- VS Code
- GitHub

## Project Structure

```text
Day-26/
│
├── input_videos/
│   ├── video1.mp4
│   ├── video2.mp4
│   └── video3.mp4
│
├── output_videos/
│   ├── video1_processed.mp4
│   ├── video2_processed.mp4
│   └── video3_processed.mp4
│
├── examples/
│   ├── original.png
│   ├── grayscale.png
│   └── edges.png
│
├── video_processing.py
├── webcam_processing.py
├── mini_project.py
├── app.py
├── requirements.txt
└── README.md
```

## Coding Practice

### 1. Video Processing

- Read a video using OpenCV.
- Displayed video frames one by one.
- Printed FPS, width, height, and total frames.
- Converted video frames into grayscale.
- Applied Gaussian Blur and Canny Edge Detection.
- Saved the processed video.

### 2. Webcam Processing

- Captured live video using a webcam.
- Displayed the original webcam feed.
- Converted frames into grayscale.
- Applied Gaussian Blur and Canny Edge Detection.
- Saved the processed webcam video.

## Mini Project – Video Processing Tool

I developed a video processing tool using OpenCV.

The application performs the following tasks:

1. Uploads and reads a video.
2. Displays the original video.
3. Converts video frames into grayscale.
4. Applies Gaussian Blur to reduce noise.
5. Applies Canny Edge Detection.
6. Displays original and processed frames side by side.
7. Saves and downloads the processed video.

## Image Processing Techniques

| Technique | Purpose |
|---|---|
| Grayscale | Converts color frames into black and white |
| Gaussian Blur | Reduces unwanted noise |
| Canny Edge Detection | Detects object boundaries and edges |

## Mandatory Challenge – Three Different Videos

I tested the video processing application using three different videos.

| Video | Processing Result |
|---|---|
| Video 1 | Detected the boundaries of moving people. |
| Video 2 | Detected car outlines and road edges. |
| Video 3 | Detected people, trees, and background edges. |

I compared the original videos with their processed outputs to understand how edge detection works in different environments.

## Streamlit Web Application

I created a web application using Streamlit and OpenCV.

### Features

- Upload videos.
- Display original videos.
- Apply grayscale conversion.
- Apply Gaussian Blur.
- Apply Canny Edge Detection.
- Display processed videos.
- Download processed output videos.

### Run the Application Locally

Install the required libraries:

```bash
pip install streamlit opencv-python-headless
```

Run the application:

```bash
streamlit run app.py
```

## Hugging Face / Streamlit App

**Public App Link:** Add your deployed application link here.

## Example Results

### Original Video

Add your original video screenshot here.

### Grayscale Image

Add your grayscale screenshot here.

### Canny Edge Detection

Add your edge detection screenshot here.

## Challenges Faced

- Understanding how OpenCV reads video frames.
- Working with video properties.
- Processing frames one by one.
- Saving processed videos with the correct FPS and dimensions.
- Handling webcam access.
- Deploying the video processing application.

## Learning Outcome

By completing Day 26, I learned how to read, process, display, and save videos using OpenCV. I also practiced real-time webcam processing and different image processing techniques.

This task improved my understanding of video processing and prepared me for upcoming computer vision topics such as object detection and object tracking.

## Conclusion

Day 26 helped me understand how video processing works in computer vision. I successfully practiced video reading, frame processing, webcam capture, Gaussian Blur, and Canny Edge Detection using Python and OpenCV.