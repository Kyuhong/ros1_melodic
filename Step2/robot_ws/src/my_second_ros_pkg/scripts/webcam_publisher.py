#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

def webcam_publisher():
    rospy.init_node('webcam_publisher', anonymous=True)
    pub = rospy.Publisher('/webcam/color_image', CompressedImage, queue_size=10)        
    cap = cv2.VideoCapture(0)

    bridge = CvBridge()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:            
            pub.publish(bridge.cv2_to_compressed_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass


