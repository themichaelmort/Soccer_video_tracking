import cv2 as cv
import numpy as np

img_path='snip.jpg'
img = cv.imread(img_path)

# Blurring is good for reducing noise (different lighting, different cameras, etc.)
# Blurring uses kernels (a box of pixels) that gets moved around the image to apply a blur to the middle pixel as a result of the surrounding pixels

# Averaging
kernel = (3,3) # The bigger the kernel, the more blurry
average = cv.blur(img, kernel)
cv.imshow('img', average)

# Gaussian Blur - weighted average
# More natural blur than straight averaging, but less blurring
sigmaX = 0 #standard deviation in the X direction
gaussian = cv.GaussianBlur(img, kernel, sigmaX)
cv.imshow('gaussian', gaussian)

# Median Blurring
# Better at removing salt & pepper (extreme) noise from image
kernel_side_size = 3 #this method assumes a 3x3 here
median = cv.medianBlur(img, kernel_side_size)
cv.imshow('median', median)

# Bilateral Blurring
# Most effective at retaining edges
diameter = 5
sigmaColor = 15 # Larger means more colors in the neighborhood considered
sigmaSpace = 15 #Larger means pixels farther away will affect the color
bilateral = cv.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)

cv.imshow('bilateral', bilateral)

cv.waitKey(0)