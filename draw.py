from email.utils import encode_rfc2231
import cv2 as cv
import numpy as np

# img = cv.imread(img_path)

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('WindowName', blank)

# 1.  Paint the image a certain color
blank[:] = 0,255,0 # Green
blank[:] = 0,0,255 # Red

# 2. Draw a rectangle
corner1 = (0,0) #upper left
corner2 = (250,250)# somewhere else # Try (blank.shape[1]//2, blank.shape[0]//2)
thickness = 2 # -1 makes a filled rectangle
cv.rectangle(blank, corner1, corner2, (0,255,0), thickness=thickness)


# 3. Draw Circle
center = (250,250)
color = (255,0,0) #blue
radius = 40
cv.circle(blank, center, radius, color, thickness=thickness)

# 4. Draw a line
end1 = (0,0)
end2 = (250,250)
color = (250,250,250) #White
cv.line(blank, end1, end2, color, thickness=thickness*4)

# 5. Add text to image
text = 'Hello World!'
scale = 1.0
color = (0,225,0)
origin = (150,350)
cv.putText(blank, text, origin, cv.FONT_HERSHEY_TRIPLEX, scale, 2)

cv.imshow('Colored', blank)

cv.waitKey(0)