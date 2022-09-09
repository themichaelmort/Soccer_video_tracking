import cv2 as cv
import numpy as np

img_path='snip.jpg'
img = cv.imread(img_path)

# Bitwise operations & then masking

# Images to play with
blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 355, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('circle', circle)
# cv.imshow('rectangle', rectangle)

# Bitwise AND (intersection of two images)
bitwise_and = cv.bitwise_and(rectangle, circle)
# cv.imshow('and', bitwise_and)

# Bitwise OR (overlap)
bitwise_or = cv.bitwise_or(rectangle, circle)
# cv.imshow('or', bitwise_or)

# Bitwsie XOR (non overlapping)
# Note: XOR = OR - AND
bitwise_xor = cv.bitwise_xor(rectangle, circle)
# cv.imshow('xor', bitwise_xor)

# Bitwise NOT (flips color)
bitwise_not = cv.bitwise_not(rectangle)
# cv.imshow('not', bitwise_not)



## Masking - commonly used in computer vision.

blank = np.zeros(img.shape[:2], dtype='uint8')

# mask has to be same size as image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('maks', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked) # Essentially treats the white as transparent and crops the rest as black

cv.waitKey(0)