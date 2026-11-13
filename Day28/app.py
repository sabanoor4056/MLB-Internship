
import cv2
import numpy as np
import gradio as gr
import os
import time

# Get the Day28 folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create output_images folder inside Day28
OUTPUT_DIR = os.path.join(BASE_DIR, "output_images")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Image Processing Function
def process_image(image, operation, brightness):

    # Check if image is uploaded
    if image is None:
        raise gr.Error("Please upload an image first!")

    # Convert image into OpenCV format
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 1. Grayscale
    if operation == "Grayscale":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # 2. Blur
    elif operation == "Blur":
        result = cv2.GaussianBlur(img, (15, 15), 0)

    # 3. Edge Detection
    elif operation == "Edge Detection":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # 4. Image Rotation
    elif operation == "Rotate":
        result = cv2.rotate(
            img, cv2.ROTATE_90_CLOCKWISE
        )

    # 5. Image Enhancement
    elif operation == "Enhancement":
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        enhanced = clahe.apply(l)
        merged = cv2.merge((enhanced, a, b))

        result = cv2.cvtColor(
            merged, cv2.COLOR_LAB2BGR
        )

    # 6. Contour Detection
    elif operation == "Contour Detection":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        contours, hierarchy = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = img.copy()

        cv2.drawContours(
            result, contours, -1, (0, 255, 0), 2
        )

    # 7. Shape Detection
    elif operation == "Shape Detection":

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blurred, 50, 150)

        contours, hierarchy = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = img.copy()

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 500:

                perimeter = cv2.arcLength(contour, True)

                approx = cv2.approxPolyDP(
                    contour, 0.04 * perimeter, True
                )

                corners = len(approx)

                if corners == 3:
                    shape = "Triangle"

                elif corners == 4:
                    x, y, w, h = cv2.boundingRect(approx)

                    ratio = w / float(h)

                    if 0.90 <= ratio <= 1.10:
                        shape = "Square"
                    else:
                        shape = "Rectangle"

                else:
                    shape = "Circle"

                cv2.drawContours(
                    result, [approx], -1, (0, 255, 0), 2
                )

                x, y, w, h = cv2.boundingRect(approx)

                cv2.putText(
                    result,
                    shape,
                    (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2
                )

    # 8. Brightness (Custom Challenge Feature)
    elif operation == "Brightness":
        result = cv2.convertScaleAbs(
            img, alpha=1, beta=int(brightness)
        )

    # 9. Thresholding (Custom Challenge Feature)
    elif operation == "Thresholding":

        gray = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )

        _, threshold = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

        result = cv2.cvtColor(
            threshold, cv2.COLOR_GRAY2BGR
        )

    else:
        raise gr.Error("Please select a valid operation!")

    # Convert result back to RGB
    output = cv2.cvtColor(
        result, cv2.COLOR_BGR2RGB
    )

    # Save processed image with unique filename
    output_path = os.path.join(
        OUTPUT_DIR,
        f"processed_{int(time.time() * 1000)}.png"
    )

    cv2.imwrite(
        output_path,
        cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
    )

    # Return three outputs to Gradio
    return image, output, output_path


# Create Gradio Interface
with gr.Blocks(title="Computer Vision Studio") as app:

    gr.Markdown(
        "# Computer Vision Image Processing Studio"
    )

    gr.Markdown(
        "Upload an image, select an operation "
        "and process your image."
    )

    with gr.Row():

        input_image = gr.Image(
            label="Upload Original Image",
            type="numpy"
        )

        output_image = gr.Image(
            label="Processed Image"
        )

    operation = gr.Dropdown(
        choices=[
            "Grayscale",
            "Blur",
            "Edge Detection",
            "Rotate",
            "Enhancement",
            "Contour Detection",
            "Shape Detection",
            "Brightness",
            "Thresholding"
        ],
        value="Grayscale",
        label="Select Image Processing Operation"
    )

    brightness = gr.Slider(
        minimum=0,
        maximum=100,
        value=30,
        step=5,
        label="Brightness Adjustment"
    )

    process_button = gr.Button("Process Image")

    download_file = gr.File(
        label="Download Processed Image"
    )

    process_button.click(
        fn=process_image,
        inputs=[
            input_image,
            operation,
            brightness
        ],
        outputs=[
            input_image,
            output_image,
            download_file
        ]
    )


# Launch Application
if __name__ == "__main__":
    app.launch()
