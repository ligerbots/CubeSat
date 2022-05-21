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

        filename = "IMG_" + str(int(time.time())) + ".jpg"
        full_filename = os.path.join(self.save_dir, filename)
        # print('saving to', full_filename)
        cv2.imwrite(full_filename, picture)
        return
