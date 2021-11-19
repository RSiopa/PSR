#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String


def callbackMessageReceived(data):
    rospy.loginfo(rospy.get_caller_id() + " %s", data.data)


def listener():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    parser.add_argument('--topic', type=str, default='A1')
    parser.add_argument('--topic2', type=str)
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('Sub', anonymous=True)

    rospy.Subscriber(args['topic'], String, callbackMessageReceived)
    if not args['topic2'] is None:
        rospy.Subscriber(args['topic2'], String, callbackMessageReceived)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()


if __name__ == '__main__':
    listener()