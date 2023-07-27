import cv2
import os

# Path to the video file
video_path = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_tracking\\bees_v2.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Create a directory to store the frames
output_dir = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\bees_v2'
os.makedirs(output_dir, exist_ok=True)

# Create the background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Threshold for motion detection
motion_threshold = 10000

# Read and save frames until the video ends
frame_count = 0
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Apply background subtraction to detect motion
    fg_mask = bg_subtractor.apply(frame)

    # Count the number of non-zero pixels (indicating motion) in the foreground mask
    motion_count = cv2.countNonZero(fg_mask)

    # Save the frame as an image file if motion is detected
    if motion_count > motion_threshold:
        frame_path = os.path.join(output_dir, f"motion_frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

# Release the video capture object and close the video file
video.release()
cv2.destroyAllWindows()

print("Frames extraction and motion detection completed!")
