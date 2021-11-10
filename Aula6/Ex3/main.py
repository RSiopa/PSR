#!/usr/bin/python3.8
# --------------------------------------------------
# Speech Recognition
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
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
        blk = np.zeros(image.shape, np.uint8)

        # Detect faces
        faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)
        blk = np.zeros(image.shape, np.uint8)

        for (x, y, w, h) in faces:
            print(w*h)
            if w * h > 50000:
                cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)

        # Generate result by blending both images (opacity of rectangle image is 0.25 = 25 %)
        image_out = cv2.addWeighted(image, 1.0, blk, 0.25, 1)
        cv2.imshow(window_name, image_out)

        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    main()