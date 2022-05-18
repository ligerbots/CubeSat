import cv2
import numpy as np
# cap = cv.VideoCapture(0)

imagefilename = "/Users/af/git/CubeSat/images/Untitled.png"

# draw_frame = numpy.zeros(shape=bgr_frame.shape, dtype=numpy.uint8)

while(1):
    # Take each frame
    # _, frame = cap.read()
    bgr_frame = cv2.imread(imagefilename)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    upper_blue = np.array([236,69,80])
    lower_blue = np.array([193,35,92])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(bgr_frame,bgr_frame, mask= mask)
    cv2.imshow('frame',bgr_frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()