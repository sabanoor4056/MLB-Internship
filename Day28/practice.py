
import os
import time
import cv2
import gradio as gr

# Get the Day28 folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create output_images folder inside Day28
OUTPUT_DIR = os.path.join(BASE_DIR, "output_images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Image Processing Function
def process_image(image, operation):

    if image is None:
        raise gr.Error("Please upload an image!")

    # Convert RGB to BGR
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 1. Grayscale
    if operation == "Grayscale":
        gray = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )
        result = cv2.cvtColor(
            gray, cv2.COLOR_GRAY2RGB
        )

    # 2. Blur
    elif operation == "Blur":
        blurred = cv2.GaussianBlur(
            img, (15, 15), 0
        )
        result = cv2.cvtColor(
            blurred, cv2.COLOR_BGR2RGB
        )

    # 3. Edge Detection
    elif operation == "Edge Detection":
        gray = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )
        edges = cv2.Canny(gray, 100, 200)
        result = cv2.cvtColor(
            edges, cv2.COLOR_GRAY2RGB
        )

    # 4. Image Rotation
    elif operation == "Rotate":
        rotated = cv2.rotate(
            img, cv2.ROTATE_90_CLOCKWISE
        )
        result = cv2.cvtColor(
            rotated, cv2.COLOR_BGR2RGB
        )

    # 5. Image Enhancement
    elif operation == "Enhancement":
        enhanced = cv2.convertScaleAbs(
            img, alpha=1.3, beta=20
        )
        result = cv2.cvtColor(
            enhanced, cv2.COLOR_BGR2RGB
        )

    # Save processed image
    
    output_path = os.path.join(
    OUTPUT_DIR,
    f"processed_{time.time_ns()}.png"
    )

    cv2.imwrite(
    output_path,
    cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
    )

    # Return processed image and download path
    return result, output_path


# Gradio Interface
with gr.Blocks() as demo:

    gr.Markdown("# Computer Vision Image Processing App")

    image = gr.Image(
        type="numpy",
        label="Upload Original Image"
    )

    operation = gr.Dropdown(
        choices=[
            "Grayscale",
            "Blur",
            "Edge Detection",
            "Rotate",
            "Enhancement"
        ],
        value="Grayscale",
        label="Select Operation"
    )

    process = gr.Button("Process Image")

    output = gr.Image(
        label="Processed Image"
    )

    download = gr.File(
        label="Download Processed Image"
    )

    process.click(
        fn=process_image,
        inputs=[image, operation],
        outputs=[output, download]
    )


# Run Application
demo.launch()
