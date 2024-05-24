#include <ros/ros.h>
#include "my_first_ros_pkg/msgMyNumber.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "number_publisher_node");
    ros::NodeHandle hNode;
    ros::Publisher pub = hNode.advertise<my_first_ros_pkg::msgMyNumber>("my_number", 5);
    
    ros::Rate loop_rate(1);
    int count = 0;
    while (ros::ok())
    {
        my_first_ros_pkg::msgMyNumber msg;
        msg.a = 1;
        msg.b = count;
        ROS_INFO("%d, %d", msg.a, msg.b);
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        count++;            
    }
    return 0;    
}
