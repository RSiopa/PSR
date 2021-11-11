#!/usr/bin/python3.8
# --------------------------------------------------
# Paint!
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

from functools import partial
import cv2
import numpy as np

drawing = False
ix = -1
iy = -1


def MouseCoord(event, x, y, flags, params, window_name, img, color):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (ix, iy), (x, y), color, 5)
            ix = x
            iy = y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), color, 5)


def main():

    white_image = np.full((400, 600, 3), 255, dtype=np.uint8)
    cv2.namedWindow("window")
    color = (255, 0, 0)

    while True:
        cv2.imshow("window", white_image)

        if cv2.waitKey(1) == ord('b'):
            color = (255, 0, 0)
        if cv2.waitKey(1) == ord('g'):
            color = (0, 255, 0)
        if cv2.waitKey(1) == ord('r'):
            color = (0, 0, 255)

        MouseCoord_paint = partial(MouseCoord, window_name="window", img=white_image, color=color)
        cv2.setMouseCallback("window", MouseCoord_paint)
        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    main()

