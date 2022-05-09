#!/usr/bin/python3

# Main program for LigerBots CubeSat picture collector
from camera import Camera
from imagewriter import ImageWriter


def main():
    '''Main program. Runs the rest'''
    cam = Camera()
    img_writer = ImageWriter("saved_images")

    picture = cam.take_picture()
    print("got image, size", picture.shape)

    #look for plastic
    
    img_writer.write_image(picture)

    return


if __name__ == '__main__':
    main()
