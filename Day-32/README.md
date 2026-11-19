
# Day-32: Smart Object Tracking System

## Project Overview
A computer vision project that detects and tracks
multiple objects in videos using YOLOv8 Nano.

## Technologies
- Python
- Google Colab
- YOLOv8 Nano
- OpenCV
- ByteTrack
- BoT-SORT
- Streamlit

## Object Tracking
Object tracking means following objects across
video frames using unique tracking IDs.

## Detection vs Tracking
Detection identifies objects in a frame.
Tracking follows those objects across multiple frames.

## Algorithms
ByteTrack is the primary tracking algorithm.
BoT-SORT is also available for comparison.

## Features
- Video upload
- Multiple object tracking
- Unique tracking IDs
- Confidence scores
- Unique object counting
- Output video download

## CPU Processing
The project uses CPU processing without GPU.

## Challenges
- Maintaining consistent IDs
- Overlapping objects
- Object disappearance
- Slow CPU processing

## How to Run

pip install -r requirements.txt

python tracking.py

streamlit run app.py

