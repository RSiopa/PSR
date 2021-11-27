#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from psr_aula8_ex3.srv import *


def talker(name):
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    # parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    # parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--topic2', type=str)
    # args = vars(parser.parse_args())
    # print(args)

    rospy.wait_for_service('set_dog_name')
    try:
        t = rospy.ServiceProxy('add_two_ints', SetDogName)
        resp1 = t(name)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [x y]" % sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        name = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s" % (x, y))