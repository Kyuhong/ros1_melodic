#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()

def show_image(img):
    cv2.imshow("Webcam Image", img)
    cv2.waitKey(3)

def image_callback(img_msg):   
    try:   
        cv_image = bridge.compressed_imgmsg_to_cv2(img_msg)
        show_image(cv_image)
    except CvBridgeError as e:
        print(e)
    
rospy.init_node('webcam_subscriber', anonymous=True)
sub = rospy.Subscriber('/webcam/color_image', CompressedImage, image_callback)
cv2.namedWindow("Webcam Image", 1)

while not rospy.is_shutdown():
    rospy.spin()

