#!/usr/bin/python3.8
# --------------------------------------------------
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

import argparse
import copy
from functools import partial

import cv2
import numpy as np


def onTrackbar(image, window_name, limits, val):
    mins = np.array([limits['B']['min'], limits['G']['min'], limits['R']['min']])
    maxs = np.array([limits['B']['max'], limits['G']['max'], limits['R']['max']])

    mins[0] = cv2.getTrackbarPos('min B/H', window_name)
    mins[1] = cv2.getTrackbarPos('min G/S', window_name)
    mins[2] = cv2.getTrackbarPos('min R/V', window_name)
    maxs[0] = cv2.getTrackbarPos('max B/H', window_name)
    maxs[1] = cv2.getTrackbarPos('max G/S', window_name)
    maxs[2] = cv2.getTrackbarPos('max R/V', window_name)

    mask_black = cv2.inRange(image, mins, maxs)
    # mask_black = ~mask_black
    # mask_black = mask_black.astype(np.bool)
    # image_gray_tmp = copy.copy(image)
    # image_gray_tmp[mask_black] = 1
    cv2.imshow(window_name, mask_black)


# def MouseCoord(event, x, y, flags, params, window_name, img):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print(x, ' ', y)
#         cv2.putText(img, str(x) + ',' +
#                     str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
#                     1, (255, 0, 0), 2)
#         cv2.imshow(window_name, img)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3a'

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert bgr to gray image (single channel)

    cv2.namedWindow(window_name)

    ranges = {'limits': {'B': {'max': 200, 'min': 100},
                         'G': {'max': 200, 'min': 100},
                         'R': {'max': 200, 'min': 100}}}

    # mins = np.array([ranges['limits']['B']['min'], ranges['limits']['G']['min'], ranges['limits']['R']['min']])
    # maxs = np.array([ranges['limits']['B']['max'], ranges['limits']['G']['max'], ranges['limits']['R']['max']])

    onTrackbar_HSV = partial(onTrackbar, image_HSV, window_name, ranges['limits'])

    cv2.createTrackbar('min B/H', window_name, 0, 255, onTrackbar_HSV)
    cv2.createTrackbar('max B/H', window_name, 0, 255, onTrackbar_HSV)
    cv2.createTrackbar('min G/S', window_name, 0, 255, onTrackbar_HSV)
    cv2.createTrackbar('max G/S', window_name, 0, 255, onTrackbar_HSV)
    cv2.createTrackbar('min R/V', window_name, 0, 255, onTrackbar_HSV)
    cv2.createTrackbar('max R/V', window_name, 0, 255, onTrackbar_HSV)


    # MouseCoord_Gray = partial(MouseCoord, window_name=window_name, img=image_HSV)
    # cv2.setMouseCallback(window_name, MouseCoord_Gray)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
