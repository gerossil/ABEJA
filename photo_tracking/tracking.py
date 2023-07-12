import cv2
from datetime import datetime
import time
from ultralytics import YOLO

# Create an instance of the YOLO model
model = YOLO('yolov8n.pt')

# Set the duration in seconds
duration = 60

# Define the start time
start_time = datetime.now()

# Open the video capture
cap = cv2.VideoCapture("https://youtu.be/Zgi9g1ksQHc")

# Define the output video writer
output_path = 'output/tracked_video.mp4'
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Track objects in the video until the desired duration is reached
while (datetime.now() - start_time).total_seconds() < duration:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection and tracking
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    results.render()

    # Convert the frame to BGR format
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame with tracked objects to the output video
    output_video.write(frame)

    # Display the frame with tracked objects
    cv2.imshow('Tracked Objects', frame)
    if cv2.waitKey(1) == ord('q'):
        break

    # Pause for a short time to avoid excessive requests
    time.sleep(0.03)

# Release the video capture and output video
cap.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
