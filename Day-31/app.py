import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from pathlib import Path
from ultralytics import YOLO

st.set_page_config(
    page_title="Road Damage Detection",
    page_icon="🚧",
    layout="wide"
)

st.title("🚧 AI-Based Road Damage Detection")
st.write("Upload an image or video to detect road damage using a custom-trained YOLO11n model.")

MODEL_PATH = Path(__file__).parent / "weights" / "best.pt"

@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

if not MODEL_PATH.exists():
    st.error("Model file not found. Please add best.pt inside the weights folder.")
    st.stop()

model = load_model()

confidence = st.slider(
    "Detection Confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.25,
    step=0.05
)

uploaded_file = st.file_uploader(
    "Upload an image or video",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"]
)

if uploaded_file is not None:

    file_extension = Path(uploaded_file.name).suffix.lower()

    if file_extension in [".jpg", ".jpeg", ".png"]:

        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is None:
            st.error("Could not read the uploaded image.")
            st.stop()

        if st.button("Detect Road Damage"):

            with st.spinner("Detecting road damage..."):
                result = model.predict(
                    source=image,
                    conf=confidence,
                    verbose=False
                )[0]

                annotated = result.plot()
                annotated_rgb = cv2.cvtColor(
                    annotated, cv2.COLOR_BGR2RGB
                )

            st.subheader("Detection Result")
            st.image(annotated_rgb, use_container_width=True)

            st.subheader("Detected Objects")

            if len(result.boxes) == 0:
                st.info("No road damage detected.")
            else:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    score = float(box.conf[0])
                    class_name = model.names[class_id]

                    st.write(
                        f"**{class_name}** — Confidence: {score:.2%}"
                    )

            success, encoded = cv2.imencode(
                ".jpg", annotated
            )

            if success:
                st.download_button(
    label="Download Processed Image",
    data=encoded.tobytes(),
    file_name="road_damage_prediction.jpg",
    mime="image/jpeg",
    on_click="ignore"
)

    elif file_extension in [".mp4", ".avi", ".mov"]:

        if st.button("Process Video"):

            input_path = None
            output_path = None

            try:
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=file_extension
                ) as input_file:
                    input_file.write(uploaded_file.getbuffer())
                    input_path = input_file.name

                cap = cv2.VideoCapture(input_path)

                fps = cap.get(cv2.CAP_PROP_FPS)
                if not fps or fps <= 0:
                    fps = 25.0

                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".mp4"
                ) as output_file:
                    output_path = output_file.name

                writer = cv2.VideoWriter(
                    output_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    fps,
                    (width, height)
                )

                if not cap.isOpened() or not writer.isOpened():
                    st.error("Could not open or process this video.")
                    st.stop()

                progress = st.progress(0)
                status = st.empty()

                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                frame_number = 0

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    result = model.predict(
                        source=frame,
                        conf=confidence,
                        verbose=False
                    )[0]

                    writer.write(result.plot())
                    frame_number += 1

                    if total_frames > 0:
                        progress.progress(
                            min(frame_number / total_frames, 1.0)
                        )

                    status.write(
                        f"Processed {frame_number} frames"
                    )

                cap.release()
                writer.release()

                if os.path.exists(output_path):
                    with open(output_path, "rb") as video_file:
                        video_bytes = video_file.read()

                    st.success("Video processing completed!")
                    st.video(video_bytes)

                    st.download_button(
                        "Download Processed Video",
                        data=video_bytes,
                        file_name="road_damage_processed.mp4",
                        mime="video/mp4"
                    )

            finally:
                if input_path and os.path.exists(input_path):
                    os.remove(input_path)

                # Keep output until the user downloads it during this run.
                # Streamlit reruns the script when the download button is used.

st.divider()
st.caption("Custom 7-class Road Damage Detection | YOLO11n | Day 31")
