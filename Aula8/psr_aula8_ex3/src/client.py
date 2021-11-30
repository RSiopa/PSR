#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from psr_aula8_ex3.srv import *

pub = None


def callback(msg):
    pub.publish(msg.name)


def client():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    global pub

    parser = argparse.ArgumentParser(description='server/client')  # arguments
    parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--topic2', type=str)
    args = vars(parser.parse_args())
    # print(args)

    rospy.init_node('client', anonymous=True)
    rospy.Subscriber('chatter', Dog, callback)

    if args['topic'] == 'set_dog_name':
        SetDogName_client()

    pub = rospy.Publisher(args['topic'], String, queue_size=10)
    rospy.spin()


def handle_SetDogName(req):
    print("Returning ", req)
    return True


def SetDogName_client():
    s = rospy.Service('set_dog_name', SetDogName, handle_SetDogName)
    print("Ready to change name")


if __name__ == '__main__':
    try:
        client()
    except rospy.ROSInterruptException:
        pass
