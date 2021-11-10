#!/usr/bin/python3.8
# --------------------------------------------------
# Speech Recognition
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import copy

import cv2
import numpy as np


def main():
    # initial setup
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    while True:
        _, image = capture.read()  # get an image from the camera
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)
        blk = np.zeros(image.shape, np.uint8)
        image_edges = cv2.Canny(image, 100, 175)
        image_red_edges = copy.deepcopy(image)
        indices = np.where(image_edges == 255)
        image_red_edges[indices[0], indices[1], :] = [0, 0, 255]

        for (x, y, w, h) in faces:

            if w * h > 50000:
                cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                image_red_edges[y:y + h, x:x + w] = image[y:y + h, x:x + w]

        # Generate result by blending both images (opacity of rectangle image is 0.25 = 25 %)
        image_rect = cv2.addWeighted(image_red_edges, 1.0, blk, 0.25, 1)

        cv2.imshow(window_name, image_rect)

        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    main()
