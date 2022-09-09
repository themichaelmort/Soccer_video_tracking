import cv2 as cv
import numpy as np

img_path='snip.jpg'
img = cv.imread(img_path)

# Split into blue, green, & red channels
b, g, r = cv.split(img)

# Check out the shape - a 2-tuple
print(b.shape)

# The image is displayed as greyscale (intensity)
# White = lots of that color
# Black = little of that color
cv.imshow('img', b)

# To display as colored, add on the missing dimensions.
# One way to do this is to just use a blank image
blank = np.zeros(b.shape, dtype='uint8')

# Then reconstruct a 3-channel image
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# merge colors back into 
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)