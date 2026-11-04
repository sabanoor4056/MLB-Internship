# Day-28: OpenCV Image Processing Toolkit

## Introduction
This project is based on image processing using Python and OpenCV. It performs different operations on images and provides a menu-driven application.

## Tools and Technologies
- Python
- OpenCV
- NumPy
- Matplotlib
- Visual Studio Code

## Programs Implemented

### OpenCV Practice
1. Read images and display dimensions, channels and file size.
2. Convert images to grayscale.
3. Resize images.
4. Crop different regions.
5. Rotate images by 90, 180 and 270 degrees.
6. Flip images horizontally and vertically.
7. Draw rectangles, circles, lines and polygons.
8. Add custom text and date.
9. Save processed images.

### Image Processing Toolkit
The application provides a menu to:
- Load an image.
- Convert to grayscale.
- Resize an image.
- Rotate an image.
- Flip an image.
- Crop an image.
- Draw shapes.
- Add custom text.
- Save processed images.

### Bonus Features
- Brightness adjustment.
- Contrast adjustment.
- RGB and BGR comparison.
- Display original and processed images side by side.

## Difference Between BGR and RGB
RGB stands for Red, Green and Blue. BGR stands for Blue, Green and Red.

OpenCV uses BGR format by default, while Matplotlib uses RGB format. We use `cv2.cvtColor()` to convert between these formats.

## What Are Grayscale Images?
Grayscale images contain only black, white and different shades of gray. They are useful for simplifying images and making some image-processing tasks easier.

## OpenCV Functions Used
- `cv2.imread()`
- `cv2.imshow()`
- `cv2.imwrite()`
- `cv2.cvtColor()`
- `cv2.resize()`
- `cv2.rotate()`
- `cv2.flip()`
- `cv2.rectangle()`
- `cv2.circle()`
- `cv2.line()`
- `cv2.polylines()`
- `cv2.putText()`
- `cv2.convertScaleAbs()`

## Challenge Task
I selected five different images:
1. Landscape
2. Person
3. Vehicle
4. Document
5. Object

I applied image-processing operations to all five images and organized the processed results into separate folders.

## Challenges Faced and Solutions
1. Understanding BGR and RGB formats: I used `cv2.cvtColor()` to convert between them.
2. Image resizing: I used `cv2.resize()` to change image dimensions.
3. Cropping images: I used image coordinates to select different regions.
4. Saving images: I used `cv2.imwrite()` and created output folders using Python's `os` module.

## Conclusion
I learned how images are represented in OpenCV and how to perform different image-processing operations. I also developed a menu-driven Image Processing Toolkit using Python and OpenCV.