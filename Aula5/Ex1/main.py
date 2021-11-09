#!/usr/bin/python3.8
# --------------------------------------------------
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

import argparse
import cv2
from readchar import readchar


def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')  # arguments
    parser.add_argument('--image1', type=str,help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

    # Process image
    retval, image_processed = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    #Visualization
    try:
        while True:
            cv2.imshow('window', image_original)
            cv2.waitKey(3000)
            cv2.imshow('window', image_processed)
            cv2.waitKey(3000)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
