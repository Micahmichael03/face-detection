# Import the OpenCV library
import cv2

# Import the randrange function from the random module
from random import randrange

# Load a pre-trained data file for detecting faces using the Haar cascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from the webcam
webcam = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually the built-in webcam)

# Iterate forever over frames
while True:
    
    # Read the current frame from the webcam
    successful_frame_read, frame = webcam.read()
    
    # Must convert the frame to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame using the trained face data
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    # Draw rectangles around the detected faces in the original color frame
    for (x, y, w, h) in face_coordinates:
        # Draw a rectangle around each face with a random color
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 2)
    
    # Display the frame with the detected faces
    cv2.imshow("Michael Programmer", frame)
    
    # Wait for a key press (1 millisecond delay)
    key = cv2.waitKey(1)
    
    # Stop the loop if the 'q' key is pressed
    if key == 81 or key == 113:
        break

# Release the videoCapture object
webcam.release()

# Print a completion message
print("Code completed")
