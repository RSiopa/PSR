#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
# from psr_aula8_ex3.srv import SetDogName, SetDogNameResponse
from colorama import Fore, Style
from colorama import init as colorama_init


# def handle_set_dog_name(req):
#     return SetDogNameResponse(req.new_name)


def talker():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------
    # parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    # parser.add_argument('--rate', type=float, default=1)
    # parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--message', type=str, default='I do not know what to say!')
    # args = vars(parser.parse_args())
    # print(args)

    colorama_init(autoreset=True)

    rospy.init_node('Pub', anonymous=True)
    # print(rate_private)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    # pub = rospy.Publisher('A17', String, queue_size=10)
    # rate = rospy.Rate(rate_private)  # 10hz

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        # message_to_send = args['message'] + ' ' + str(rospy.get_time())
        # rospy.loginfo(message_to_send)
        # pub.publish(message_to_send)

        rate_private = rospy.get_param('~rate', default=10)
        rate = rospy.Rate(rate_private)

        dog = Dog()
        dog.name = 'max'
        # s = rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)
        dog.age = 10
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('bobby')
        dog.header.stamp = rospy.Time.now()

        color = rospy.get_param('highlight_text_color')
        rospy.loginfo(getattr(Fore, str(color)) + 'Dog info incoming...' + Style.RESET_ALL)
        pub.publish(dog)

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
