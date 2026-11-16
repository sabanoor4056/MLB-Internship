
---
title: Simple OCR Document Reader
emoji: 📄
sdk: streamlit
app_file: app.py
---

# Day 29 - OCR Document Reader

## Introduction
OCR stands for Optical Character Recognition.
It converts text inside images into editable digital text.

## Library Used
I used EasyOCR because it is beginner-friendly,
supports multiple languages, and uses deep learning
to recognize text in images.

## Image Preprocessing
I used:
- Grayscale conversion
- Contrast enhancement

These techniques helped improve text visibility.

## OCR Applications
- Reading documents
- Reading receipts
- Reading invoices
- Reading signboards
- Digitizing books

## Challenges
- Blurry images
- Poor lighting
- Small text
- Handwriting recognition
- Incorrect text detection

## Multithreading Support

- Tesseract: Supports CPU multithreading
  through OpenMP-enabled builds.
- EasyOCR: Uses PyTorch and can be used in
  concurrent processing workflows, but its
  basic readtext() call does not automatically
  process multiple images in parallel.
- PaddleOCR: Supports parallel inference
  in supported configurations, including
  multiple devices and multiprocessing.

## Project Features
- Upload an image
- Extract text using EasyOCR
- Display original image
- Display extracted text
- Download extracted text as TXT

## Technologies
- Python
- EasyOCR
- streamlit
- Pillow
- NumPy

## Dataset
Used 15 different images containing text.

