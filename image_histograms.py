import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_path='snip.jpg'
img = cv.imread(img_path)

# Histograms let you visualize the distribution of intensities in the image

# Greyscale Histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale histogram (with optional masking)
blank = np.zeros(img.shape[:2], dtype='uint8')
radius = 250
center = (blank.shape[1]//2, blank.shape[0]//2)
circle = cv.circle(blank, center, radius, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
pixel_val_range = [0, 256]
gray_hist = cv.calcHist([gray], [0], mask, [256], pixel_val_range)

# cv.imshow('mask', mask)

plt.figure()
plt.title('Grayscale Historgram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
# plt.show()

# Color Histogram
colors = ('b', 'g', 'r')
mask = None
plt.figure()
plt.title('Color Historgram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], pixel_val_range)
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.legend(colors)
plt.show()

cv.waitKey(0)