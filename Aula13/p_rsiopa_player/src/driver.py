#!/usr/bin/env python3
import copy
import math

import rospy
import tf2_ros
from geometry_msgs.msg import PoseStamped, Twist
import tf2_geometry_msgs


class Driver:

    def __init__(self):

        self.goal = PoseStamped()
        self.goal_active = False

        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)
        self.publisher_command = rospy.Publisher('/p_rsiopa/cmd_vel', Twist, queue_size=1)
        self.timer = rospy.Timer(rospy.Duration(0.1), self.sendCommandCallback)
        self.goal_subscriber = rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goalReceivedCallback)

    def goalReceivedCallback(self, goal_msg):

        self.goal = goal_msg
        self.goal_active = True

    def sendCommandCallback(self, msg):

        if self.goal_active:

            distance_to_goal = self.computeDintanceToGoal(self.goal)

            if distance_to_goal < 0.05:
                rospy.logwarn('I have achieved my goal!')
                self.goal_active = False

        if self.goal_active:

            angle, speed = self.driveStraight(self.goal)
            if angle is None or speed is None:
                angle = 0
                speed = 0
        else:
            angle = 0
            speed = 0

        command_msg = Twist()
        command_msg.linear.x = speed
        command_msg.angular.z = angle
        self.publisher_command.publish(command_msg)

    def computeDintanceToGoal(self, goal):

        goal_present_time = copy.deepcopy(goal)
        goal_present_time.header.stamp = rospy.Time.now()

        target_frame = 'p_rsiopa/base_link'
        try:
            goal_in_base_link = self.tf_buffer.transform(goal_present_time, target_frame, rospy.Duration(1))
        except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logerr('Could not transform goal from ' + goal.header.frame_id + ' to ' + target_frame + '.')
            return None, None

        x = goal_in_base_link.pose.position.x
        y = goal_in_base_link.pose.position.y

        distance = math.sqrt(x**2 + y**2)
        return distance

    def driveStraight(self, goal, minimum_speed=0.1, maximum_speed=0.5):

        goal_present_time = copy.deepcopy(goal)
        goal_present_time.header.stamp = rospy.Time.now()

        target_frame = 'p_rsiopa/base_link'
        try:
            goal_in_base_link = self.tf_buffer.transform(goal_present_time, target_frame, rospy.Duration(1))
        except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logerr('Could not transform goal from ' + goal.header.frame_id + ' to ' + target_frame + '.')
            return None, None

        x = goal_in_base_link.pose.position.x
        y = goal_in_base_link.pose.position.y

        angle = math.atan2(y, x)

        distance = math.sqrt(x**2 + y**2)
        speed = 0.5 * distance

        speed = min(speed, maximum_speed)
        speed = max(speed, minimum_speed)

        return angle, speed


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------

    rospy.init_node('p_rsiopa_driver', anonymous=False)

    driver = Driver()
    rospy.spin()


if __name__ == '__main__':
    main()
