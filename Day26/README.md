
# Day-25: Edge Detection and Morphological Operations

## 1. Topics Covered
- Edge Detection
- Sobel Operator
- Laplacian Operator
- Canny Edge Detection
- Gaussian Blur
- Morphological Operations
- Contour Detection

## 2. Edge Detection Methods

- Sobel: Detects horizontal and vertical edges.
- Laplacian: Detects edges in all directions.
- Canny: Produces clean and thin edges.

## 3. Morphological Operations

- Erosion: Shrinks white objects.
- Dilation: Expands white objects.
- Opening: Removes small white noise.
- Closing: Fills small gaps.
- Gradient: Highlights object boundaries.
- Top Hat: Highlights bright details.
- Black Hat: Highlights dark details.

## 4. Mini Project

Document Boundary Detection Tool using OpenCV.

The project:
1. Loads document images.
2. Converts images to grayscale.
3. Applies Gaussian Blur.
4. Detects edges using Canny.
5. Applies morphological closing.
6. Finds the largest contour.
7. Draws the detected boundary.
8. Saves the final output.

## 5. Dataset

Used 10 different document images with
different conditions, including tilted,
blurred, and shadowed documents.

## 6. Best Results

Canny Edge Detection with Gaussian Blur
and Morphological Closing gave useful
results for document boundary detection.

## 7. Challenges

- Shadows affected edge detection.
- Blurred images made boundaries difficult.
- Some contours were incomplete.
- Different threshold values affected results.

## 8. Tools Used

- Python
- OpenCV
- NumPy
- VS Code

## 9. Conclusion

Learned how to detect edges, apply
morphological operations, and detect
document boundaries using OpenCV.
