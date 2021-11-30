#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from psr_aula8_ex3.srv import SetDogName, SetDogNameResponse

Dog_name = 'boby'


def callback(msg):
    print('The name of the dog is ' + msg.data)


def server_SetDogName(dog):
    rospy.wait_for_service('set_dog_name')
    try:
        Dog_name = rospy.ServiceProxy('set_dog_name', SetDogName)
        resp = Dog_name(dog)
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def server():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------
    global Dog_name

    parser = argparse.ArgumentParser(description='server/client')  # arguments
    # parser.add_argument('--rate', type=float, default=1)
    parser.add_argument('--topic', type=str, default='A1')
    parser.add_argument('--dog_name', type=str, default='boby')
    args = vars(parser.parse_args())
    # print(args)

    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    rospy.init_node('server', anonymous=True)
    rospy.Subscriber(args['topic'], String, callback)
    # rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)
    rate = rospy.Rate(1)  # 10hz

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        # message_to_send = args['message'] + ' ' + str(rospy.get_time())
        # rospy.loginfo(message_to_send)
        # pub.publish(message_to_send)

        dog = Dog()

        if args['topic'] == 'set_dog_name':
            server_SetDogName(args['dog_name'])

        dog.name = Dog_name

        dog.age = 10
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('max')

        pub.publish(dog)
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        server()
    except rospy.ROSInterruptException:
        pass
