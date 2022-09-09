import cv2 as cv
import numpy as np

img_path='snip.jpg'
img = cv.imread(img_path)

# Thresholding is a way to make a mask or binarize an image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Simple Thresholding
thresholding_value = 150 #Values above this number go to max value, otherwise they go to 0
max_value = 255 #Set to max to binarize the image
threshold, thresh = cv.threshold(gray, thresholding_value, max_value, cv.THRESH_BINARY)
cv.imshow('simgple Threshold', thresh)

# Inverse values
threshold, thresh_inv = cv.threshold(gray, thresholding_value, max_value, cv.THRESH_BINARY_INV)
cv.imshow('simgple Inverse Threshold', thresh_inv)


# Adapted Thresholding
block_size = 9
c_value = 3 # integer subtracted from the mean, more accurate with larger numbers
method = cv.ADAPTIVE_THRESH_GAUSSIAN_C #cv.ADAPTIVE_THRESH_MEAN_C #both work
adaptive_thresh = cv.adaptiveThreshold(gray, max_value, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c_value)
cv.imshow('adaptive', adaptive_thresh)

cv.waitKey(0)