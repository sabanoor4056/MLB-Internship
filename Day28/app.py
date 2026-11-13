import cv2
import numpy as np
import streamlit as st
import os
import time
import subprocess
import sys
from PIL import Image

# Page Settings
st.set_page_config(
    page_title="Computer Vision Studio",
    page_icon="📸",
    layout="wide"
)


# Folder Settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "output_images")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# Image Processing Function
def process_image(image, operation, brightness):

    if image is None:
        return None

    img = cv2.cvtColor(
        np.array(image.convert("RGB")),
        cv2.COLOR_RGB2BGR
    )

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

    # 4. Rotate
    elif operation == "Rotate":

        result = cv2.rotate(
            img,
            cv2.ROTATE_90_CLOCKWISE
        )

    # 5. Enhancement
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
            merged,
            cv2.COLOR_LAB2BGR
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
            result,
            contours,
            -1,
            (0, 255, 0),
            2
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
                    contour,
                    0.04 * perimeter,
                    True
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
                    result,
                    [approx],
                    -1,
                    (0, 255, 0),
                    2
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

    # 8. Brightness
    elif operation == "Brightness":

        result = cv2.convertScaleAbs(
            img,
            alpha=1,
            beta=int(brightness)
        )

    # 9. Thresholding
    elif operation == "Thresholding":

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(
            gray,
            127,
            255,
            cv2.THRESH_BINARY
        )

        result = cv2.cvtColor(
            threshold,
            cv2.COLOR_GRAY2BGR
        )

    else:
        return None

    # Convert BGR to RGB
    output = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # Save Image
    output_path = os.path.join(
        OUTPUT_DIR,
        f"processed_{int(time.time() * 1000)}.png"
    )

    cv2.imwrite(
        output_path,
        cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
    )

    return output, output_path


# Streamlit Interface

st.title("📸 Computer Vision Image Processing Studio")

st.write(
    "Upload an image, select an operation "
    "and process your image."
)

st.divider()


# Upload Image
uploaded_file = st.file_uploader(
    "Upload Original Image",
    type=["jpg", "jpeg", "png"]
)


# Select Operation
operation = st.selectbox(
    "Select Image Processing Operation",
    [
        "Grayscale",
        "Blur",
        "Edge Detection",
        "Rotate",
        "Enhancement",
        "Contour Detection",
        "Shape Detection",
        "Brightness",
        "Thresholding"
    ]
)


# Brightness Slider
brightness = st.slider(
    "Brightness Adjustment",
    min_value=0,
    max_value=100,
    value=30,
    step=5
)


# Process Image Button
if st.button("Process Image", type="primary"):

    if uploaded_file is None:

        st.error("Please upload an image first!")

    else:

        try:

            image = Image.open(uploaded_file).convert("RGB")

            result = process_image(
                image,
                operation,
                brightness
            )

            if result is not None:

                output, output_path = result

                st.subheader("Image Results")

                col1, col2 = st.columns(2)

                with col1:

                    st.image(
                        image,
                        caption="Original Image",
                        use_container_width=True
                    )

                with col2:

                    st.image(
                        output,
                        caption="Processed Image",
                        use_container_width=True
                    )

                # Download Button
                with open(output_path, "rb") as file:

                    st.download_button(
                        label="Download Processed Image",
                        data=file.read(),
                        file_name="processed_image.png",
                        mime="image/png"
                    )

                st.success("Image processed successfully!")

        except Exception as e:

            st.error(f"An error occurred: {e}")