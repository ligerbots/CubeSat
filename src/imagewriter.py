#!/usr/bin/python3

import os.path
import time
import cv2


class ImageWriter:
    '''Write image to storage, if we want to keep it'''

    def __init__(self, save_dir_arg):
        self.save_dir = save_dir_arg
        return

    def write(self, picture):
        '''Write the picture to a file'''

        # shrink the picture by 2x
        small_pic = cv2.resize(picture, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        filename = "IMG_" + str(int(time.time())) + ".jpg"
        full_filename = os.path.join(self.save_dir, filename)
        # print('saving to', full_filename)

        # write out the image, but set the JPEG quality to 50 to reduce the size
        cv2.imwrite(full_filename, small_pic, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
        return
