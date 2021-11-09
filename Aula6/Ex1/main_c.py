#!/usr/bin/python3.8
# --------------------------------------------------
# Paint!
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import argparse
import copy
from functools import partial

import cv2
import numpy as np


def MouseCoord(event, x, y, flags, params, window_name, img):

    if event == cv2.EVENT_LBUTTONDBLCLK:

        cv2.circle(img, (x, y), 1, (255, 0, 0), 1)

        cv2.imshow(window_name, img)


def main():

    white_image = np.full((400, 600, 3), 255, dtype=np.uint8)
    cv2.namedWindow("window")

    MouseCoord_paint = partial(MouseCoord, window_name="window", img=white_image)
    cv2.setMouseCallback("window", MouseCoord_paint)

    while True:
        cv2.imshow("window", white_image)


if __name__ == '__main__':
    main()

