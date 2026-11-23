
import streamlit as st
import os
import tempfile
import uuid
import hashlib

from people_counting import process_video, process_image


# PAGE CONFIGURATION

st.set_page_config(
    page_title="PeopleVision AI | Crowd Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# SESSION STATE

if "analysis_result" not in st.session_state:
    st.session_state["analysis_result"] = None

if "upload_hash" not in st.session_state:
    st.session_state["upload_hash"] = None


# CUSTOM CSS

st.markdown("""
<style>

/* Main application */

.stApp {
    background: #0B1020;
    color: #F1F5F9;
}

/* Main content */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #11182B;
    border-right: 1px solid #26324A;
}

section[data-testid="stSidebar"] * {
    color: #E2E8F0;
}

/* Main headings */

h1, h2, h3, h4 {
    color: #F8FAFC !important;
}

/* Paragraphs */

p {
    color: #B8C4D8;
}

/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #131D32;
    border: 1px solid #283651;
    border-radius: 14px;
}

/* Metric cards */

div[data-testid="stMetric"] {
    background: #17243A;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #30405D;
}

/* Metric values */

div[data-testid="stMetricValue"] {
    color: #A78BFA;
}

/* Buttons */

.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #6366F1);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    width: 100%;
    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #6D28D9, #4F46E5);
    color: white;
    border: none;
}

/* Download buttons */

.stDownloadButton > button {
    background: #17243A;
    color: #C4B5FD;
    border: 1px solid #8B5CF6;
    border-radius: 9px;
    width: 100%;
}

/* Upload area */

div[data-testid="stFileUploader"] {
    background: #131D32;
    border: 1px dashed #64748B;
    border-radius: 12px;
    padding: 15px;
}

/* Divider */

hr {
    border-color: #283651;
}

/* Project header */

.hero {
    background: linear-gradient(
        120deg,
        #1E1B4B,
        #172554,
        #17243A
    );
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #39466B;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.hero-description {
    font-size: 15px;
    color: #C7D2FE;
}

.tag {
    display: inline-block;
    background: #312E81;
    color: #DDD6FE;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    margin: 4px 4px 4px 0;
}

.section-heading {
    font-size: 21px;
    font-weight: 700;
    color: #F8FAFC;
    margin-bottom: 15px;
}

.info-box {
    background: #131D32;
    border: 1px solid #283651;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
}

.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 12px;
    padding: 25px 0 10px 0;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:

    st.markdown("# 👥 PeopleVision AI")

    st.caption("INTELLIGENT CROWD ANALYTICS")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "About Project"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### ⚙️ System Information")

    st.markdown("""
    **AI Model:** YOLO11n

    **Tracking:** ByteTrack

    **Processing:** OpenCV

    **Interface:** Streamlit
    """)

    st.divider()

    st.markdown("### 🟢 System Status")

    st.success("Application Ready")

    st.caption("Day 33 | MLB Internship")


# DASHBOARD PAGE

if page == "Dashboard":

    # Hero section

    
    st.markdown("""
<div class="hero-title">
    👥 PeopleVision AI
</div>

<div class="hero-description">
    Smart People Detection, Tracking
    and Crowd Analytics Dashboard
</div>

<br>

<span class="tag">YOLO Detection</span>
<span class="tag">ByteTrack Tracking</span>
<span class="tag">Real-Time Frame Analysis</span>
<span class="tag">Crowd Analytics</span>
""", unsafe_allow_html=True)



    # Upload section

    st.markdown(
        '<div class="section-heading">📁 Upload Your Media</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        input_type = st.selectbox(
            "Select Media Type",
            ["Image", "Video"]
        )

    with col2:

        if input_type == "Image":

            st.info("Supported formats: JPG, JPEG, PNG")

        else:

            st.info("Supported formats: MP4, AVI, MOV")


    # File uploader

    if input_type == "Image":

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"],
            key="image_upload"
        )

    else:

        uploaded_file = st.file_uploader(
            "Choose a video",
            type=["mp4", "avi", "mov"],
            key="video_upload"
        )


    # File processing

    if uploaded_file is not None:

        uploaded_bytes = uploaded_file.getvalue()

        # Check uploaded file

        current_hash = hashlib.sha256(
            uploaded_bytes
        ).hexdigest()

        if current_hash != st.session_state["upload_hash"]:

            st.session_state["analysis_result"] = None

            st.session_state["upload_hash"] = current_hash


        st.divider()

        st.markdown(
            '<div class="section-heading">📂 Input Preview</div>',
            unsafe_allow_html=True
        )

        preview_col, details_col = st.columns([1.5, 1])

        with preview_col:

            if input_type == "Image":

                st.image(
                    uploaded_bytes,
                    caption="Uploaded Image",
                    use_container_width=True
                )

            else:

                st.video(uploaded_bytes)


        with details_col:

            st.markdown("### File Information")

            st.write("**Filename:**", uploaded_file.name)

            st.write(
                "**File Size:**",
                f"{len(uploaded_bytes) / (1024 * 1024):.2f} MB"
            )

            st.write("**Media Type:**", input_type)

            st.write("**Status:** Uploaded successfully")

            st.success("Ready for AI Analysis")


        st.divider()


        # Processing button

        if st.button(
            "🚀 Start AI Detection",
            type="primary",
            use_container_width=True
        ):

            input_path = None
            output_path = None

            try:

                # Create temporary input file

                suffix = os.path.splitext(
                    uploaded_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp:

                    temp.write(uploaded_bytes)

                    input_path = temp.name


                # Create output folders

                os.makedirs(
                    "output_images",
                    exist_ok=True
                )

                os.makedirs(
                    "output_videos",
                    exist_ok=True
                )


                # Generate output filename

                unique_id = uuid.uuid4().hex[:8]


                # Select output path

                if input_type == "Image":

                    output_path = os.path.join(
                        "output_images",
                        f"processed_image_{unique_id}.jpg"
                    )

                else:

                    output_path = os.path.join(
                        "output_videos",
                        f"processed_video_{unique_id}.mp4"
                    )


                # Run AI processing

                with st.spinner(
                    "AI is detecting and analyzing people... Please wait."
                ):

                    if input_type == "Image":

                        count = process_image(
                            input_path,
                            output_path
                        )

                        result_data = {
                            "type": "Image",
                            "count": count,
                            "output": output_path
                        }

                    else:

                        result = process_video(
                            input_path,
                            output_path,
                            show_window=False
                        )

                        result_data = {
                            "type": "Video",
                            "unique": result["unique_people"],
                            "peak": result["peak_occupancy"],
                            "output": output_path
                        }


                # Save results

                st.session_state["analysis_result"] = result_data

                st.success(
                    "AI Analysis Completed Successfully!"
                )


            except Exception as e:

                st.error(
                    f"Processing failed: {e}"
                )

                st.session_state["analysis_result"] = None


            finally:

                # Remove temporary file

                if input_path and os.path.exists(input_path):

                    os.remove(input_path)


    # Results section

    result_data = st.session_state.get(
        "analysis_result"
    )

    if result_data is not None:

        st.divider()

        st.markdown(
            '<div class="section-heading">📊 Detection Analytics</div>',
            unsafe_allow_html=True
        )


        # Image results

        if result_data["type"] == "Image":

            st.metric(
                "Total People Detected",
                result_data["count"]
            )


        # Video results

        else:

            col1, col2 = st.columns(2)

            col1.metric(
                "Unique People Tracked",
                result_data["unique"]
            )

            col2.metric(
                "Peak Occupancy",
                result_data["peak"]
            )


        # Processed output

        st.divider()

        st.markdown(
            '<div class="section-heading">🎯 Processed Output</div>',
            unsafe_allow_html=True
        )

        output_path = result_data["output"]


        if os.path.exists(output_path):

            if result_data["type"] == "Image":

                st.image(
                    output_path,
                    caption="AI Processed Image",
                    use_container_width=True
                )

                with open(output_path, "rb") as file:

                    st.download_button(
                        "⬇️ Download Processed Image",
                        data=file.read(),
                        file_name="processed_image.jpg",
                        mime="image/jpeg"
                    )


            else:

                st.video(output_path)

                with open(output_path, "rb") as file:

                    st.download_button(
                        "⬇️ Download Processed Video",
                        data=file.read(),
                        file_name="processed_video.mp4",
                        mime="video/mp4"
                    )

        else:

            st.warning(
                "Output file is no longer available. "
                "Please run detection again."
            )


    else:

        st.info(
            "Please upload an image or video to start people detection."
        )


# ABOUT PROJECT PAGE

elif page == "About Project":

    # About section

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
            About PeopleVision AI
        </div>

        <div class="hero-description">
            An AI-powered system for detecting,
            tracking and analyzing people in images and videos.
        </div>

    </div>
    """, unsafe_allow_html=True)


    # Project objective

    st.markdown("### 🎯 Project Objective")

    st.write("""
    PeopleVision AI is designed to automatically identify
    people in images and videos, track their movement
    and provide useful crowd analytics.

    The system uses YOLO for detection, ByteTrack
    for tracking and OpenCV for image and video processing.
    """)


    # Technologies used

    st.markdown("### 🛠️ Technologies Used")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="info-box">

            <h4>🤖 YOLO</h4>

            Detects people in images and video frames.

        </div>

        <div class="info-box">

            <h4>🔄 ByteTrack</h4>

            Tracks detected people using unique IDs.

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="info-box">

            <h4>📷 OpenCV</h4>

            Processes images and videos and draws bounding boxes.

        </div>

        <div class="info-box">

            <h4>🌐 Streamlit</h4>

            Provides the interactive web application.

        </div>
        """, unsafe_allow_html=True)


    # Main features

    st.markdown("### ✨ Main Features")

    st.write("""
    - People detection in images and videos
    - Unique person tracking IDs
    - Bounding boxes and confidence scores
    - Visible people counting
    - Peak occupancy calculation
    - Processed output download
    """)


    # Real-world applications

    st.markdown("### 🌍 Real-World Applications")

    st.write("""
    - Shopping mall crowd monitoring
    - Office occupancy monitoring
    - Classroom and campus analytics
    - Public area crowd management
    - Building entrance monitoring
    """)


    # Future improvements

    st.markdown("### 🚀 Future Improvements")

    st.write("""
    - Entry and exit counting
    - Region of Interest (ROI)
    - Improved tracking accuracy
    - Real-time CCTV monitoring
    - Crowd density analysis
    """)


# FOOTER

st.markdown("""
<div style="text-align: center;">
    <p>Built with Python, YOLO, OpenCV and Streamlit</p>
    <p>Machine Learning &amp; Computer Vision Internship</p>
</div>
""", unsafe_allow_html=True)


