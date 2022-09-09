from math import comb
import cv2 as cv
import numpy as np

img_path='snip.jpg'
img = cv.imread(img_path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian Method
# From multivariable clac recall that the Laplacian operator returns the sum of the pure second partial derivatives.
data_depth = cv.CV_64F
lap = cv.Laplacian(gray, data_depth)
lap = np.uint8(np.absolute(lap))
# Transitions have high gradients

cv.imshow('Laplacian', lap)


# Sobel Method
# - Computes the gradient in X and in Y
# - Canny Edge Detection Uses Sobel as a part of the processing.
x_direction = 1
y_direction = 0
sobelx = cv.Sobel(gray, data_depth, x_direction, y_direction)
cv.imshow('Soble X', sobelx)

x_direction = 0
y_direction = 1
sobely = cv.Sobel(gray, data_depth, x_direction, y_direction)
cv.imshow('Sobel Y', sobely)

# Comined
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)


cv.waitKey(0)