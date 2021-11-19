#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String


def talker():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------
    parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    parser.add_argument('--rate', type=float, default=1)
    parser.add_argument('--topic', type=str, default='A1')
    parser.add_argument('--message', type=str, default='I do not know what to say!')
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('Pub', anonymous=True)
    pub = rospy.Publisher(args['topic'], String, queue_size=10)
    rate = rospy.Rate(args['rate']) # 10hz

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        message_to_send = args['message'] + ' ' + str(rospy.get_time())
        rospy.loginfo(message_to_send)
        pub.publish(message_to_send)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass