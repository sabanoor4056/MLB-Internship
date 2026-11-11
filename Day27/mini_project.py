
import cv2
import os

# Get current project folder
base_folder = os.path.dirname(os.path.abspath(__file__))

# Input and output folders
input_folder = os.path.join(base_folder, "mini_input")
output_folder = os.path.join(base_folder, "mini_output")

# Create output folder if needed
os.makedirs(output_folder, exist_ok=True)

# Three input videos
videos = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4"
]

# Process all videos
for video_name in videos:

    print("\nProcessing:", video_name)

    # Read video
    video_path = os.path.join(input_folder, video_name)
    cap = cv2.VideoCapture(video_path)

    # Check video
    if not cap.isOpened():
        print("Error: Cannot open", video_name)
        continue

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("FPS:", fps)
    print("Width:", width)
    print("Height:", height)
    print("Total Frames:", total_frames)

    if fps <= 0:
        fps = 20

    # Create output filename
    output_name = video_name.replace(
        ".mp4", "_processed.mp4"
    )

    output_path = os.path.join(
        output_folder, output_name
    )

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width * 2, height)
    )

    if not out.isOpened():
        print("Error: Cannot create output video")
        cap.release()
        continue

    # Read frames one by one
    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        # Apply Gaussian Blur
        blur = cv2.GaussianBlur(
            gray, (5, 5), 0
        )

        # Apply Canny Edge Detection
        edges = cv2.Canny(
            blur, 100, 200
        )

        # Convert edges to 3 channels
        edges_color = cv2.cvtColor(
            edges, cv2.COLOR_GRAY2BGR
        )

        # Combine original and processed frames
        combined = cv2.hconcat([
            frame, edges_color
        ])

        # Display video
        cv2.imshow(
            "Original | Processed Video",
            combined
        )

        # Save processed video
        out.write(combined)

        # Press Q to stop current video
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("Saved successfully:", output_path)

print("\nAll videos processing completed!")
