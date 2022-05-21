#!/usr/bin/python3

import cv2
import numpy


class PlasticFinder:
    '''class to process an image and look for plastic'''

    def __init__(self):
        self.low_blue = numpy.array([85, 5, 20])
        self.high_blue = numpy.array([150, 255, 255])
        
        self.low_white = numpy.array([0, 30, 30])
        self.high_white = numpy.array([255, 255, 255])
        return

    def process(self, picture):
        
        # first, convert to HSV for better color selection
        hsv_frame = cv2.cvtColor(picture, cv2.COLOR_BGR2HSV)
        
        # select the blue pixels
        blue_mask = cv2.inRange(hsv_frame, self.low_blue, self.high_blue)
        # invert to get "not blue"
        not_blue_mask = cv2.bitwise_not(blue_mask)
        
        # select the white pixels
        white_mask = cv2.inRange(hsv_frame, self.low_white, self.high_white)
        
        # combine the masks
        full_mask = cv2.bitwise_and(white_mask, not_blue_mask)
        
        # mask off both to leave pixels which are not blue and not white
        # masked_frame = cv2.bitwise_and(picture, picture, mask=full_mask)
        
        # find the regions that are left
        res = cv2.findContours(full_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(res) == 2:
            contours = res[0]
        else:
            contours = res[1]

        # find the size and location of the regions
        # remove some contours
        contour_data = []
        accepted_contours = []
        for cnt in contours:
            M = cv2.moments(cnt)
            area = M['m00']
            # ignore small regions
            if area < 50:
                continue

            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
            # we want to remove regions right on edges
            x,y,w,h = cv2.boundingRect(cnt)
            if x <= 1:  # or y <= 1:
                continue
            if (x+w) > (picture.shape[1] - 3):  # or (y+h) > picture.shape[0] - 3:
                continue
            
            # done. Keep it
            accepted_contours.append(cnt)
            contour_data.append( ((cx, cy), area) )
           
        # create an image with the plastic outlined in red
        out_frame = numpy.zeros(shape=picture.shape, dtype=numpy.uint8)
        numpy.copyto(out_frame, picture)
        cv2.drawContours(out_frame, accepted_contours, -1, (0, 0, 255), 3)

        #numpy.copyto(out_frame, masked_frame)
        
        return out_frame, contour_data


if __name__ == '__main__':
    import argparse
    import os.path
    import sys
    
    parser = argparse.ArgumentParser(description='Test the plastic finder')
    parser.add_argument('input_files', nargs='+', help='Input image files')

    args = parser.parse_args()

    if sys.platform == "win32":
        # windows does not expand the "*" files on the command line
        #  so we have to do it.
        import glob

        infiles = []
        for f in args.input_files:
            infiles.extend(glob.glob(f))
        args.input_files = infiles

    finder = PlasticFinder()
    
    for infile in args.input_files:
        bgr_frame = cv2.imread(infile)
        out_image, data = finder.process(bgr_frame)

        outfile = os.path.join('output', os.path.basename(infile))
        cv2.imwrite(outfile, out_image)
        
        #print(data)
        