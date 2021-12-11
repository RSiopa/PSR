#!/usr/bin/python3.8
# --------------------------------------------------
# Video Acquisition
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def main():
    # initial setup
    rospy.init_node('CameraToROS')

    pub = rospy.Publisher('image', Image, queue_size=10)

    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    while True:
        _, image_cv2 = capture.read()  # get an image from the camera

        cv2.imshow(window_name, image_cv2)

        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(image_cv2, "bgr8")

        pub.publish(image_message)

        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    main()
