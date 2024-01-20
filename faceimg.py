# Import the OpenCV library
import cv2

# Import the randrange function from the random module
from random import randrange

# Load a pre-trained data file for detecting faces using the Haar cascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
img = cv2.imread('dog.webp')  # Read an image using OpenCV

# Convert the image to grayscale as Haar cascade works on grayscale images
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image using the trained face data
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the detected faces in the original color image
for (x, y, w, h) in face_coordinates:
    # Draw a rectangle around each face with a random color
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 2)

# Display the image with the detected faces
cv2.imshow("Michael Programmer", img)

# Wait for a key press and store the key code
key = cv2.waitKey()

# Print a completion message
print("Code completed")
