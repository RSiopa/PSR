#!/usr/bin/env python3
# --------------------------------------------------
# Python script for color adjustment and saving the values to a json file.
# Rafael Inacio Siopa.
# Frederico Ribeiro e Martins.
# Rodrigo Dinis Martins Ferreira.
# Bartosz Bartosik.
# PSR, November 2021.
# --------------------------------------------------
import json
import cv2
import numpy as np


def nothing(x):
    pass


def main():
    window_name = 'window - Ex3a'
    cv2.namedWindow(window_name)
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FPS, 15)

    ranges = {'limits': {'H': {'max': 255, 'min': 0},
                         'S': {'max': 255, 'min': 0},
                         'V': {'max': 255, 'min': 0}}}

    cv2.createTrackbar('min H', window_name, 0, 255, nothing)
    cv2.createTrackbar('max H', window_name, 255, 255, nothing)
    cv2.createTrackbar('min S', window_name, 0, 255, nothing)
    cv2.createTrackbar('max S', window_name, 255, 255, nothing)
    cv2.createTrackbar('min V', window_name, 0, 255, nothing)
    cv2.createTrackbar('max V', window_name, 255, 255, nothing)

    while True:
        _, image = capture.read()
        image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        mins = np.array([ranges['limits']['B']['min'], ranges['limits']['G']['min'], ranges['limits']['R']['min']])
        maxs = np.array([ranges['limits']['B']['max'], ranges['limits']['G']['max'], ranges['limits']['R']['max']])

        ranges['limits']['B']['min'] = mins[0] = cv2.getTrackbarPos('min B', window_name)
        ranges['limits']['G']['min'] = mins[1] = cv2.getTrackbarPos('min G', window_name)
        ranges['limits']['R']['min'] = mins[2] = cv2.getTrackbarPos('min R', window_name)
        ranges['limits']['B']['max'] = maxs[0] = cv2.getTrackbarPos('max B', window_name)
        ranges['limits']['G']['max'] = maxs[1] = cv2.getTrackbarPos('max G', window_name)
        ranges['limits']['R']['max'] = maxs[2] = cv2.getTrackbarPos('max R', window_name)

        mask_black = cv2.inRange(image_HSV, mins, maxs)
        cv2.imshow(window_name, mask_black)

        if cv2.waitKey(1) == ord('w'):
            file_name = 'limits.json'
            with open(file_name, 'w') as file_handle:
                print('writing dictionary ranges to file ' + file_name)
                json.dump(ranges, file_handle)  # d is the dictionary

        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    main()
