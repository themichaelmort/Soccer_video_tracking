
"""
Swithing between color spaces - systems of representing colors
RGB, Grayscale, HSV, LAB
"""

import cv2 as cv
from matplotlib import pyplot as plt

img_path='snip.jpg'
img = cv.imread(img_path)

# BGR (Blue Green Red) to Grayscale
# Grayscale shows you the distribution of intensities in an image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV - Hue Saturation Value, similar to human perception
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to LAB - L x A x B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)


# BGR to RGB (when you have problems with color inversion)
# matplotlib assumes RGB color order
rgb = cv.cvt.Color(img, cv.COLOR_BGR2RGB)


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)


# cv.imshow('snip_img', lab)

cv.waitKey(0)