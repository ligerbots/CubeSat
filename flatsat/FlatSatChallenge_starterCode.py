#!/usr/bin/python3

# complete CAPITALIZED sections

# AUTHOR: LigerBots CubeSat team
# DATE: 3/14/2022

# import libraries
import time
import os
import board
import busio
import adafruit_bno055
# from git import Repo
from picamerax import PiCamera
import math

# setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()

"""
#bonus: function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge') #PATH TO YOUR GITHUB REPO
        repo.git.add('folder path') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
"""

 
#SET THRESHOLD
threshold = 15.0

camera.resolution = (1920, 1080)
# awb_mode = 'greyworld' is only in picameraX
camera.awb_mode = 'greyworld'

# this blocks the whole screen, so not too helpful
# camera.start_preview()

while True:
    # read acceleration
    accelX, accelY, accelZ = sensor.acceleration
    # print(accelX, accelY, accelZ)
    totalAccel = math.sqrt(accelX**2 + accelY**2 + accelZ**2)
    print('totalAccel =', totalAccel)

    # CHECK IF READINGS ARE ABOVE THRESHOLD
    if totalAccel > threshold:
        print('Picture triggered')

        # PAUSE - count down 5 to 1
        for countdown in range(5, 0, -1):
            print(countdown)
            time.sleep(1)

        # TAKE/SAVE/UPLOAD A PICTURE 
        name = "ligerbots"     #Last Name, First Initial  ex. FoxJ

        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/CubeSat/flatsat/Images/%s%s.jpg' % (name,t))

            print('Taking picture', imgname)
            camera.capture(imgname)

    # PAUSE
    time.sleep(1)
