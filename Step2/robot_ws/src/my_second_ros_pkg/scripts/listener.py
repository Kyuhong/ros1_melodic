#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo('I heard %s', msg.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('say', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
