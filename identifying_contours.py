import cv2 as cv
import numpy as np

im_path = ''
img = cv.imread(im_path)

#Convert to BW
gray = cv.cvtColor(img, cv.COLOR_BGR2BGRAY)


## OPTION 1: Blur & canny edge
# Blur to simplify number of contours
kernel = (5,5)
blur = cv.GaussianBlur(gray, kernel, cv.BORDER_DEFAULT)

# Get canny edges
canny = cv.Canny(blur, 125, 175, cv.THRESH_BINARY)

# Find the contours 
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countour(s) found.')


## OPTION 2: Threshold with Binarization

# Binarize image (if below a threshold set to black, if above, white)
max = 255
threshold_val = 125
ref, thresh = cv.threshold(gray, threshold_val, max)

# Find the contours 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countour(s) found.')


# cv.RETR_TREE = all the hirearchical contours
# cv.RETR_EXTERNAL = all the external contours
# cv.RETR_LIST = all the contours in the image
# 
# cv.CHAIN_APPROX_NONE - get all the pixels
# cv.CHAIN_APPROX_SIMPLE - approximate simple shapes with general representations (a line = to end points)

# Draw ablank image
blank = np.zeros(img.shape, dtype='uint8')

# Draw Contours found onto black image
contours_index = -1 #all of them
color = (0, 0, 255) # red
thickness = 2 #2 pixels
cv.drawContours(blank, contours, contours_index, color, thickness)

cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

# General Recommendation: Canny first + find contours, rather than thresholding first.