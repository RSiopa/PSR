#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from colorama import Fore, Style
from colorama import init as colorama_init

def callbackMessageReceived(msg):
    color = rospy.get_param('/highlight_text_color')
    rospy.loginfo('Received a dog named ' + getattr(Fore, str(color)) + msg.name + Style.RESET_ALL + ' which is ' +
                  getattr(Fore, str(color)) + str(msg.age) + Style.RESET_ALL + ' years old')


def listener():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    # parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    # parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--topic2', type=str)
    # args = vars(parser.parse_args())
    # print(args)

    colorama_init(autoreset=True)

    rospy.init_node('Sub', anonymous=True)

    rospy.Subscriber('chatter', Dog, callbackMessageReceived)
    # if not args['topic2'] is None:+ getattr(Fore, str(color))
    #     rospy.Subscriber(args['topic2'], String, callbackMessageReceived)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()


if __name__ == '__main__':
    listener()
