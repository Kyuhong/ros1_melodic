#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def node_publisher():
    rospy.init_node('turtle_move', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)   
 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        move_msg = Twist()
        move_msg.linear.x = 2.0
        move_msg.linear.y = 0.0
        move_msg.linear.z = 0.0
        move_msg.angular.x = 0.0
        move_msg.angular.y = 0.0
        move_msg.angular.z = 1.0

        rospy.loginfo('cmd_vel: l_x=%d, a_z=%d'%(move_msg.linear.x, move_msg.angular.z))
        pub.publish(move_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        node_publisher()
    except rospy.ROSInterruptException:
        pass
