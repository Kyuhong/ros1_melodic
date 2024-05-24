#!/usr/bin/env python3

import rospy
from my_first_ros_pkg.msg import msgMyNumber

def number_publisher():
    rospy.init_node('number_publisher', anonymous=True)
    pub = rospy.Publisher('my_number', msgMyNumber, queue_size=10)    
    rate = rospy.Rate(10) # 10hz
    count = 0
    while not rospy.is_shutdown():
        msg_number = msgMyNumber()     
        msg_number.a = 2
        msg_number.b = count
        count += 1
        print_str = "msg : a=%d, b=%d" % (msg_number.a, msg_number.b)
        rospy.loginfo(print_str)
        pub.publish(msg_number)
        rate.sleep()

if __name__ == '__main__':
    try:
        number_publisher()
    except rospy.ROSInterruptException:
        pass