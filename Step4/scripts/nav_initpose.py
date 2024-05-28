#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler


x = 0.0
y = 0.0
yaw = 0.0


rospy.init_node("initalpose_publisher_node")
pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10)

initpose = PoseWithCovarianceStamped()
initpose.header.stamp = rospy.get_rostime()
initpose.header.frame_id = "map"
initpose.pose.pose.position.x = x
initpose.pose.pose.position.y = y
initpose.pose.pose.position.z = 0

quaternion = quaternion_from_euler(0, 0, yaw)

initpose.pose.pose.orientation.x = quaternion[0]
initpose.pose.pose.orientation.y = quaternion[1]
initpose.pose.pose.orientation.z = quaternion[2]
initpose.pose.pose.orientation.w = quaternion[3]

pub.publish(initpose)

