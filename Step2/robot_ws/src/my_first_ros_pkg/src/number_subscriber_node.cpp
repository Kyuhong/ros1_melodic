#include <ros/ros.h>
#include "my_first_ros_pkg/msgMyNumber.h"

void msgCallback(const my_first_ros_pkg::msgMyNumber::ConstPtr& msg)
{
    ROS_INFO("receive msg: %d, %d", msg->a, msg->b);
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "number_subscriber_node");
    ros::NodeHandle hNode;
    ros::Subscriber sub = hNode.subscribe("my_number", 10, msgCallback);
    
    ros::spin();
    return 0;    
}
