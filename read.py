"""
Learning to use open cv (computer vision) 
from YouTube:
https://www.youtube.com/watch?v=oXlwWbU8l2o
"""


import cv2 as cv

# # Reading Images
# path_to_im = ''
# img = cv.imread(path_to_im)
# window_name = 'Displayed Image'
# cv.imshow(window_name, img)

# cv.waitKey(0)



# # Reading in Videos

# # capture = cv.VideoCapture(0) # for using hardware on your computer
# path_to_vid = r'clips\0a2d9b_0.mp4'
# capture = cv.VideoCapture(path_to_vid)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     # If you press d, stop loop
#     if cv.waitKey(10) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


## Rescaling Frame (for videos, live videos and images)
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

path_to_vid = r'clips\0a2d9b_0.mp4'
capture = cv.VideoCapture(path_to_vid)
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    print(frame_resized.shape)
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # If you press d, stop loop
    if cv.waitKey(10) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()



# Change live video resolution
def changeRes(width, height):
    capture.set(3,width) #int 3 access the width attribute
    capture.set(4,height) #int 4 access the height attribute