#include <ros/ros.h>
#include <std_msgs/String.h>

void msgCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("receive msg: %s", msg->data.c_str());
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "hello_world_subscriber_node");
    ros::NodeHandle hNode;

    ros::Subscriber sub = hNode.subscribe("hello_world", 10, msgCallback);
    
    ros::spin();
    return 0;    
}
