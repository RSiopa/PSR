#!/usr/bin/python3.8
# --------------------------------------------------
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import argparse
import cv2

def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')  # arguments
    parser.add_argument('--image1', type=str,help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image_b, image_g, image_r = cv2.split(image_rgb)

    # Process image
    _, image_b_processed = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    _, image_g_processed = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    _, image_r_processed = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)
    image_processed = cv2.merge((image_b_processed, image_g_processed, image_r_processed))

    # Visualization
    cv2.imshow('window', image_rgb)
    cv2.imshow('processed b', image_b_processed)
    cv2.imshow('processed g', image_g_processed)
    cv2.imshow('processed r', image_r_processed)
    cv2.imshow('final', image_processed)

    cv2.waitKey(8000)


if __name__ == '__main__':
    main()
