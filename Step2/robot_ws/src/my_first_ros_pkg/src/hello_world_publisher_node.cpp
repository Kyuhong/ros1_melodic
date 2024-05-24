#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "hello_world_publisher_node");
    ros::NodeHandle hNode;
    ros::Publisher pub = hNode.advertise<std_msgs::String>("hello_world", 5);
    
    ros::Rate loop_rate(10);
    int count = 0;
    while (ros::ok())
    {
        std_msgs::String msg;
        std::stringstream ss;
        ss << "hello world : " << count;
        msg.data = ss.str();
        ROS_INFO("%s", msg.data.c_str());
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }
    return 0;    
}
