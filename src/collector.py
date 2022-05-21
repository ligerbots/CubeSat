#!/usr/bin/python3

# Main program for LigerBots CubeSat picture collector
from camera import Camera
from imagewriter import ImageWriter
from datawriter import DataWriter
from plasticfinder import PlasticFinder
from imureader import ImuReader
import time


def main():
    '''Main program. Runs the rest'''
    cam = Camera()
    img_writer = ImageWriter("saved_images")
    data_writer = DataWriter("saved_images")
    finder = PlasticFinder()
    imu = ImuReader()
    
    while True:
        print('taking picture')
        picture = cam.take_picture()
        
        # look for plastic
        out_picture, contour_data = finder.process(picture)
        
        out_data = {'orientation': imu.get_orientation(),
                    'contours': contour_data,
                    'time': time.gmtime()}
        
        img_writer.write(out_picture)
        data_writer.write(out_data)
        
        time.sleep(5)

    return


if __name__ == '__main__':
    main()
