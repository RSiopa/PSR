#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog

def callbackMessageReceived(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def listener():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    # parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    # parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--topic2', type=str)
    # args = vars(parser.parse_args())
    # print(args)

    rospy.init_node('Sub', anonymous=True)

    rospy.Subscriber('chatter', Dog, callbackMessageReceived)
    # if not args['topic2'] is None:
    #     rospy.Subscriber(args['topic2'], String, callbackMessageReceived)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()


if __name__ == '__main__':
    listener()