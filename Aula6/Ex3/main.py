#!/usr/bin/python3.8
# --------------------------------------------------
# Speech Recognition
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import audioop
import copy
import pyaudio
import cv2
import numpy as np
from colorama import Fore, Style


def main():
    # initial setup
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

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
        area = 0
        max_area = 0

        data = stream.read(CHUNK)

        for (x, y, w, h) in faces:
            area = w * h
            if area > max_area:
                max_area = area
                cv2.rectangle(blk, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                image_red_edges[y:y + h, x:x + w] = image[y:y + h, x:x + w]
                rms = audioop.rms(data, 2)
                print(str(rms))

                if rms > 100:
                    print(Fore.RED + 'Someone is speaking!' + Style.RESET_ALL)
                else:
                    print(Fore.BLUE + 'I am all alone!' + Style.RESET_ALL)

        # Generate result by blending both images (opacity of rectangle image is 0.25 = 25 %)
        image_rect = cv2.addWeighted(image_red_edges, 1.0, blk, 0.25, 1)

        cv2.imshow(window_name, image_rect)

        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    main()
