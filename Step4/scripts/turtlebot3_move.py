#!/usr/bin/env python3

import rospy
from pynput import keyboard
from geometry_msgs.msg import Twist


vx = 0.0
az = 0.0 


def node_publisher():
    global vx, az
    rospy.init_node('turtlebot3_move', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)   
 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        move_msg = Twist()
        move_msg.linear.x = vx
        move_msg.linear.y = 0.0
        move_msg.linear.z = 0.0
        move_msg.angular.x = 0.0
        move_msg.angular.y = 0.0
        move_msg.angular.z = az

        rospy.loginfo('cmd_vel: l_x=%d, a_z=%d'%(move_msg.linear.x, move_msg.angular.z))
        pub.publish(move_msg)
        rate.sleep()


if __name__ == '__main__':

    def on_release(key):
        global vx, az

        print('release:', key)
        if key == keyboard.Key.up or key == keyboard.Key.down:
            vx = 0.0
        elif key == keyboard.Key.left or key == keyboard.Key.right:
            az = 0.0


    def on_press(key):
        global vx, az

        print('press:', key)
        if key == keyboard.Key.up:
            vx = 0.2
        elif key == keyboard.Key.down:
            vx = -0.2
        elif key == keyboard.Key.left:
            az = 0.2
        elif key == keyboard.Key.right:
            az = -0.2       


    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keyboard_listener.start()


    try:
        node_publisher()
    except rospy.ROSInterruptException:
        pass
