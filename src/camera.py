#!/usr/bin/python3

# Routines to take a picture
from picamerax import PiCamera
import numpy as np
import time


class Camera:
    '''Handle the Pi camera and take pictures'''

    def __init__(self):
        '''Initialize camera'''

        self.pi_camera = PiCamera()
        self.pi_camera.resolution = (1920, 1088)

        # set "auto-white-balance" to "greyworld", to deal with pink images
        self.pi_camera.awb_mode = 'greyworld'
        
        time.sleep(5)
        return

    def take_picture(self):
        '''Take a picture and return it'''

        # create empty array to hold the image
        image = np.empty((1920 * 1088 * 3,), dtype=np.uint8)

        # capture image, in order BGR
        self.pi_camera.capture(image, 'bgr')

        # shape into the correct image shape
        image = image.reshape((1088, 1920, 3))

        # return image
        return image
