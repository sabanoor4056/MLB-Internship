
# Day 33 - Smart People Counting System

## Project Overview
This project uses YOLO and OpenCV to detect and count people in images and videos.

## Technologies Used
- Python
- YOLO
- OpenCV
- ByteTrack
- Streamlit

## Features
- People detection in images and videos
- Bounding boxes around detected people
- Confidence scores
- Unique tracking IDs
- Live people counting
- Peak occupancy calculation
- Download processed images and videos

## How It Works
YOLO detects people in images and video frames.
ByteTrack assigns tracking IDs to detected people.
OpenCV draws bounding boxes and displays the people count.

## Detection vs Counting
Detection identifies people in an image or video.
Counting calculates how many people are visible.

## Challenges
- Overlapping people
- Crowded scenes
- Poor lighting
- People hiding behind other people

## Future Improvements
- Entry and exit counting
- Region of Interest (ROI)
- Better tracking accuracy
- Real-time camera monitoring

## How to Run

Install libraries:

pip install -r requirements.txt

Run people detection:

python people_counting.py

Run Streamlit application:

streamlit run app.py
