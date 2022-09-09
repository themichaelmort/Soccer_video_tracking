import cv2 as cv
import numpy as np

# Open CV has lots of pretrained classifiers
# https://www.youtube.com/watch?v=oXlwWbU8l2o&t=2737s

img_path='snip.jpg'
img = cv.imread(img_path)

# Crop image to mostly be the pitch
cropped = img[125:,:,:]
# cv.imshow('cropped', cropped)


# Convert to Grayscale
gray = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Gaussian Blur - weighted average
# More natural blur than straight averaging, but less blurring
kernel = (7,7)
sigmaX = 0 #standard deviation in the X direction
gaussian = cv.GaussianBlur(gray, kernel, sigmaX)


# Load classifier model
haar_cascade = cv.CascadeClassifier('haar_body.xml')

# RUn Model
bodies_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.001, minNeighbors=2)

# Number of people
print(f"Number of people {len(bodies_rect)}. Truth: 22.")


# Draw bounding boxes
box_color = (0, 255, 0) # Green
thickness = 2
for (x, y, w, h) in bodies_rect:
    cv.rectangle(cropped, (x,y), (x+w, y+h), box_color, thickness)

cv.imshow('Detected', cropped)

cv.waitKey(0)