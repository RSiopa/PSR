#!/usr/bin/env python3
import argparse

import sensor_msgs.point_cloud2 as pc2
import rospy
import std_msgs.msg
from sensor_msgs import point_cloud2
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
import laser_geometry.laser_geometry as lg
import math

# pc_pub = None
# lp = None
pub = rospy.Publisher("/lidar_subscriber/point_cloud", PointCloud2, queue_size=1)


def callback(msg):

    rospy.loginfo('LaserScan message received')
    header = std_msgs.msg.Header(seq=msg.header.seq, stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)]

    points = []
    z=0
    for idx, range in enumerate(msg.ranges):
        theta = msg.angle_min + idx * msg.angle_increment
        x = range * math.cos(theta)
        y = range * math.sin(theta)
        points.append((x, y, z))

    # pcloud = PointCloud2()
    pcloud = point_cloud2.create_cloud(header, fields, points)
    # pcloud.header = header
    # pcloud.fields = fields
    # pcloud.data = points
    pub.publish(pcloud)

    # global pc_pub, lp

    # rospy.loginfo('LaserScan message received')
    # # convert the message of type LaserScan to a PointCloud2
    # pc2_msg = lp.projectLaser(msg)
    #
    # # now we can do something with the PointCloud2 for example:
    # # publish it
    # pc_pub.publish(pc2_msg)
    #
    # # convert it to a generator of the individual points
    # point_generator = pc2.read_points(pc2_msg)
    #
    # # we can access a generator in a loop
    # sum = 0.0
    # num = 0
    # for point in point_generator:
    #     if not math.isnan(point[2]):
    #         sum += point[2]
    #         num += 1
    # # we can calculate the average z value for example
    # print(str(sum / num))
    #
    # # or a list of the individual points which is less efficient
    # point_list = pc2.read_points_list(pc2_msg)
    #
    # # we can access the point list with an index, each element is a namedtuple
    # # we can access the elements by name, the generator does not yield namedtuples!
    # # if we convert it to a list and back this possibility is lost
    # print(point_list[int(len(point_list) / 2)].x)


def lidar_subscriber():
    #------------------------------------------------
    #Initialization
    # ------------------------------------------------

    # global pc_pub, lp

    rospy.init_node('PolarToCartesian')
    # lp = lg.LaserProjection()
    # pc_pub = rospy.Publisher("/lidar_subscriber/point_cloud", PointCloud2, queue_size=1)
    # sub = rospy.Subscriber('/left_laser/laserscan', LaserScan, callback, queue_size=1)
    rospy.Subscriber('/left_laser/laserscan', LaserScan, callback, queue_size=1)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()


if __name__ == '__main__':
    try:
        lidar_subscriber()
    except rospy.ROSInterruptException:
        pass
