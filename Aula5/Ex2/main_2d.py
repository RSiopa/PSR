#!/usr/bin/python3
import argparse
import copy

import cv2
import numpy as np

def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')  # arguments
    parser.add_argument('--image1', required=True, type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    ranges = {'b': {'min': 0, 'max': 50},
              'g': {'min': 80, 'max': 150},
              'r': {'min': 0, 'max': 50}}

    # Process image
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    image_processed = cv2.inRange(image_rgb, mins, maxs)

    # ranges = {'h': {'min': 40, 'max': 80},
    #           's': {'min': 170, 'max': 256},
    #           'v': {'min': 70, 'max': 150}}
    #
    # # Process image
    # mins = np.array([ranges['h']['min'], ranges['s']['min'], ranges['v']['min']])
    # maxs = np.array([ranges['h']['max'], ranges['s']['max'], ranges['v']['max']])
    # image_processed = cv2.inRange(image_hsv, mins, maxs)

    mask = image_processed.astype(np.bool)
    image_green_changed = copy.deepcopy(image_rgb)
    image_green_changed[mask] = (0, 0, 255)

    # Visualization
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', image_rgb)
    # cv2.imshow('original', image_hsv)
    cv2.namedWindow('image_processed', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image_processed', image_processed)
    cv2.namedWindow('image_green_changed', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image_green_changed', image_green_changed)

    cv2.waitKey(8000)


if __name__ == '__main__':
    main()
