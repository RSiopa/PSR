import argparse
import copy
from functools import partial

import cv2
import numpy as np


def onTrackbarMin(minimum, image, window_name):
    mask_black = cv2.inRange(image, 0, minimum)
    mask_black = ~mask_black
    mask_black = mask_black.astype(np.bool)
    image_gray_tmp = copy.copy(image)
    image_gray_tmp[mask_black] = 0
    cv2.imshow(window_name, image_gray_tmp)


def onTrackbarMax(maximum, image, window_name):
    mask_black = cv2.inRange(image, maximum, 255)
    mask_black = ~mask_black
    mask_black = mask_black.astype(np.bool)
    image_gray_tmp = copy.copy(image)
    image_gray_tmp[mask_black] = 1
    cv2.imshow(window_name, image_gray_tmp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3a'

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    onTrackbarMin_Gray = partial(onTrackbarMin, image=image_gray, window_name='window - Ex3a')
    onTrackbarMax_Gray = partial(onTrackbarMax, image=image_gray, window_name='window - Ex3a')

    cv2.createTrackbar('Red', window_name, 0, 255, onTrackbarMin_Gray)
    cv2.createTrackbar('Red2', window_name, 0, 255, onTrackbarMax_Gray)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()