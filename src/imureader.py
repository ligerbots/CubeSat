#/usr/bin/python3

import board
import busio
import adafruit_bno055


class ImuReader:
    '''Read the IMU and return orientation'''

    def __init__(self):
        # setup imu and camera
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        return

    def get_orientation(self):
        return self.sensor.euler


if __name__ == "__main__":
    import time
    
    imu = ImuReader()
    while True:
        print(imu.get_orientation())
        time.sleep(1)