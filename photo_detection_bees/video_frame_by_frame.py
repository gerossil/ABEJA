import cv2
import os

# Path to the video file
video_path = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_tracking\\bees_v9.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Create a directory to store the frames
output_dir = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\bees\\bees_v9'
os.makedirs(output_dir, exist_ok=True)

# Read and save frames until the video ends
frame_count = 0
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Save the frame as an image file
    frame_path = os.path.join(output_dir, f"bees_v9_{frame_count}.jpg")
    cv2.imwrite(frame_path, frame)

    frame_count += 1

# Release the video capture object and close the video file
video.release()
cv2.destroyAllWindows()

print("Frames extraction completed!")
