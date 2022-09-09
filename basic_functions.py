import cv2 as cv
import numpy as np

img = np.random.randint(0,high=255, size=(500,500,3), dtype='uint8')



# Convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray.shape) # We lose a dimension 

# Blur image
kernel_size = (3,3)
img = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

# Edge Cascade (edge detection filter)
threshold1= 125
threshold2 = 175
# Pass in a blurred images to get rid of texture edges
img = cv.Canny(img, threshold1, threshold2)

# Dilate the image (especially one with edges detected)
dilated = cv.dilate(img, (3,3), iterations=1)

# Erode the image
eroded = cv.erode(dilated, (3,3), iterations=1)

# Resize an image
destimation_size = (50,50)
# INTER_AREA good for making smaller
# INTER_CUBIC good for increasing (though slow, high quality)
# INTER_LINEAR good for increasing (fast, low quality)
resized = cv.resize(img, destimation_size, interpolation=cv.INTER_AREA)

# Cropping
cropped = img[50:200, 200:400]

# Translating images (if -x = left, +x=right, -y = up, +y=down)
def translate(img, x, y):
        transMat = np.float32([1,0,x], [0,1,y])
        dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img.transMat, dimensions)

# Rotating images (-angle = cw, +angle = ccw)
def rotate(img, angle, rotPoint=None):
        (height,width) = img.shape[:2]

        if rotPoint is None:
                rotPoint = (width//2, height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMat, dimensions)

# Flipping the image - 0=vertical, 1=horizontall, -1=both
flip = cv.flip(img, 0) 


cv.imshow("Window", img)
cv.waitKey(0)