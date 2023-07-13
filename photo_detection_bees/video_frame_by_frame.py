import cv2
import os

# Path to the video file
video_path = 'C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection_bees\\video-zoomed_10s.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Create a directory to store the frames
output_dir = 'C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection_bees\\path_to_output_directory'
os.makedirs(output_dir, exist_ok=True)

# Read and save frames until the video ends
frame_count = 0
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Save the frame as an image file
    frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
    cv2.imwrite(frame_path, frame)

    frame_count += 1

# Release the video capture object and close the video file
video.release()
cv2.destroyAllWindows()

print("Frames extraction completed!")
