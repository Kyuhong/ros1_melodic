#!/usr/bin/env python3

import rospy
from my_first_ros_pkg.msg import msgMyNumber

def callback(msg):
    rospy.loginfo('I heard a=%d, b=%d', msg.a, msg.b)

def number_subscriber():
    rospy.init_node('number_subscriber', anonymous=True)
    rospy.Subscriber('my_number', msgMyNumber, callback)
    rospy.spin()

if __name__ == '__main__':
    number_subscriber()
