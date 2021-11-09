#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for anotations in images
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import argparse
import copy
import cv2


def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR)

    # Processing
    height, width, channels = image.shape
    image_circle = copy.deepcopy(image)
    image_circle = cv2.circle(image_circle, (int(width/2), int(height/2)), int(height/2), (255, 0, 0), 1)
    image_circle_text = copy.deepcopy(image_circle)
    image_circle_text = cv2.putText(image_circle_text, 'PSR', (0, height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    # Visualization
    cv2.imshow('window', image)
    cv2.imshow('window_circle', image_circle)
    cv2.imshow('window_circle_text', image_circle_text)
    cv2.waitKey(10000)

if __name__ == '__main__':
    main()

