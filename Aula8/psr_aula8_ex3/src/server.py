#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from psr_aula8_ex3.srv import SetDogName, SetDogNameResponse


def handle_set_dog_name(req):
    return SetDogNameResponse(req.new_name)


def server():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------
    # parser = argparse.ArgumentParser(description='Definition of test mode')  # arguments
    # parser.add_argument('--rate', type=float, default=1)
    # parser.add_argument('--topic', type=str, default='A1')
    # parser.add_argument('--message', type=str, default='I do not know what to say!')
    # args = vars(parser.parse_args())
    # print(args)

    rospy.init_node('Pub', anonymous=True)
    s = rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)
    rate = rospy.Rate(1)  # 10hz

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        # message_to_send = args['message'] + ' ' + str(rospy.get_time())
        # rospy.loginfo(message_to_send)
        # pub.publish(message_to_send)

        dog = Dog()
        dog.name = 'max'
        dog.age = 10
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('bobby')

        rospy.loginfo('Dog info incoming...')
        # pub.publish(dog)

        rospy.spin()


if __name__ == '__main__':
    server()
