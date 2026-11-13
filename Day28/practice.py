
import os
import time
import cv2
import numpy as np
import streamlit as st
import subprocess
import sys


# Automatically start Streamlit
if __name__ == "__main__" and not os.environ.get("STREAMLIT_RUN"):

    env = os.environ.copy()
    env["STREAMLIT_RUN"] = "1"

    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        os.path.abspath(__file__)
    ], env=env)

    sys.exit()


# Page Settings
st.set_page_config(
    page_title="Computer Vision Practice",
    page_icon="📸",
    layout="wide"
)


# Get Day28 folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create output_images folder
OUTPUT_DIR = os.path.join(BASE_DIR, "output_images")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# Image Processing Function
def process_image(image, operation):

    if image is None:
        st.error("Please upload an image!")
        return

    # Convert RGB to BGR
    img = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )

    # 1. Grayscale
    if operation == "Grayscale":

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        result = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2RGB
        )

    # 2. Blur
    elif operation == "Blur":

        blurred = cv2.GaussianBlur(
            img,
            (15, 15),
            0
        )

        result = cv2.cvtColor(
            blurred,
            cv2.COLOR_BGR2RGB
        )

    # 3. Edge Detection
    elif operation == "Edge Detection":

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(
            gray,
            100,
            200
        )

        result = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2RGB
        )

    # 4. Image Rotation
    elif operation == "Rotate":

        rotated = cv2.rotate(
            img,
            cv2.ROTATE_90_CLOCKWISE
        )

        result = cv2.cvtColor(
            rotated,
            cv2.COLOR_BGR2RGB
        )

    # 5. Image Enhancement
    elif operation == "Enhancement":

        enhanced = cv2.convertScaleAbs(
            img,
            alpha=1.3,
            beta=20
        )

        result = cv2.cvtColor(
            enhanced,
            cv2.COLOR_BGR2RGB
        )

    else:
        return None, None

    # Save processed image
    output_path = os.path.join(
        OUTPUT_DIR,
        f"processed_{time.time_ns()}.png"
    )

    cv2.imwrite(
        output_path,
        cv2.cvtColor(
            result,
            cv2.COLOR_RGB2BGR
        )
    )

    return result, output_path


# Streamlit Interface
st.title("📸 Computer Vision Image Processing App")

st.write(
    "Upload an image and select an operation "
    "to process your image."
)

st.divider()


# Upload Image
image = st.file_uploader(
    "Upload Original Image",
    type=["jpg", "jpeg", "png"]
)


# Select Operation
operation = st.selectbox(
    "Select Operation",
    [
        "Grayscale",
        "Blur",
        "Edge Detection",
        "Rotate",
        "Enhancement"
    ]
)


# Process Button
if st.button("Process Image", type="primary"):

    if image is None:

        st.error("Please upload an image!")

    else:

        try:

            # Read uploaded image
            file_bytes = np.frombuffer(
                image.getvalue(),
                np.uint8
            )

            original = cv2.imdecode(
                file_bytes,
                cv2.IMREAD_COLOR
            )

            original = cv2.cvtColor(
                original,
                cv2.COLOR_BGR2RGB
            )

            # Process image
            result, output_path = process_image(
                original,
                operation
            )

            if result is not None:

                st.subheader("Image Results")

                col1, col2 = st.columns(2)

                with col1:

                    st.image(
                        original,
                        caption="Original Image",
                        use_container_width=True
                    )

                with col2:

                    st.image(
                        result,
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

                st.info(
                    f"Saved in: {output_path}"
                )

        except Exception as e:

            st.error(f"Error: {e}")
