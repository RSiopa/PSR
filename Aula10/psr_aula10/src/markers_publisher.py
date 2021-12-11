#!/usr/bin/python3.8

from visualization_msgs.msg import Marker, MarkerArray
import rospy


def talker():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------

    rospy.init_node('register', anonymous=False)
    publisher = rospy.Publisher('markers', MarkerArray, queue_size=10)
    rospy.Rate(10)
    idx = 0
    increment = 0.1

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------

    while not rospy.is_shutdown():
        marker_array = MarkerArray()

        # Sphere
        marker_sphere = Marker()
        marker_sphere.header.frame_id = "map"
        marker_sphere.type = marker_sphere.SPHERE
        marker_sphere.action = marker_sphere.ADD
        marker_sphere.ns = 'sphere'
        marker_sphere.scale.x = 1
        marker_sphere.scale.y = 1
        marker_sphere.scale.z = 1
        marker_sphere.color.a = 0.5
        marker_sphere.color.r = 0
        marker_sphere.color.g = 1
        marker_sphere.color.b = 0
        marker_sphere.pose.orientation.w = 1
        marker_sphere.pose.orientation.x = 0
        marker_sphere.pose.orientation.y = 0
        marker_sphere.pose.orientation.z = 0
        marker_sphere.pose.position.x = idx
        marker_sphere.pose.position.y = 0
        marker_sphere.pose.position.z = 0

        marker_array.markers.append(marker_sphere)

        # Cube
        marker_cube = Marker()
        marker_cube.header.frame_id = "map"
        marker_cube.type = marker_cube.CUBE
        marker_cube.action = marker_cube.ADD
        marker_cube.ns = 'cube'
        marker_cube.scale.x = abs(idx)
        marker_cube.scale.y = abs(idx)
        marker_cube.scale.z = abs(idx)
        marker_cube.color.a = 1
        marker_cube.color.r = 1
        marker_cube.color.g = 0
        marker_cube.color.b = 0
        marker_cube.pose.orientation.w = 1
        marker_cube.pose.orientation.x = 0
        marker_cube.pose.orientation.y = 0
        marker_cube.pose.orientation.z = 0
        marker_cube.pose.position.x = 0
        marker_cube.pose.position.y = 0
        marker_cube.pose.position.z = 0

        marker_array.markers.append(marker_cube)

        # Text
        marker_text = Marker()
        marker_text.header.frame_id = "map"
        marker_text.type = marker_text.TEXT_VIEW_FACING
        marker_text.action = marker_text.ADD
        marker_text.ns = 'text'
        marker_text.text = 'Radius: 1'
        marker_text.scale.x = 0.5
        marker_text.scale.y = 0.5
        marker_text.scale.z = 0.5
        marker_text.color.a = 1
        marker_text.color.r = 1
        marker_text.color.g = 1
        marker_text.color.b = 0
        marker_text.pose.orientation.w = 1
        marker_text.pose.orientation.x = 30
        marker_text.pose.orientation.y = 0
        marker_text.pose.orientation.z = 0
        marker_text.pose.position.x = 1
        marker_text.pose.position.y = 1
        marker_text.pose.position.z = 1

        marker_array.markers.append(marker_text)

        rospy.loginfo('I am publishing')
        publisher.publish(marker_array)

        rospy.sleep(0.01)
        idx += increment
        if idx >= 3 or idx < -3:
            increment = -increment


if __name__ == '__main__':
    talker()