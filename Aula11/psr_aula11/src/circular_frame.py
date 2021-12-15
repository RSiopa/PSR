#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('circular_frame')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    parent = rospy.get_param('~parent')
    child = rospy.get_param('~child')
    distance = rospy.get_param('~distance')
    velocity = rospy.get_param('~velocity')
    t.header.frame_id = parent
    t.child_frame_id = child

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        x = rospy.Time.now().to_sec() * math.pi * velocity * 0.01

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = distance * math.sin(x)
        t.transform.translation.y = distance * math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        br.sendTransform(t)
        rate.sleep()
