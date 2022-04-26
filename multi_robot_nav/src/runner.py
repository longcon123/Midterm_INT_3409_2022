#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

dis = 0.7

def callback(msg):
    move.angular.z = 0.3
    if msg.ranges[300] > dis:
        move.linear.x = 0.3
        move.angular.z = 0.0
    
    if msg.ranges[300] <= dis:
        move.linear.x = 0
        move.angular.z = 0.3
    
    pub.publish(move)

rospy.init_node('follow_node')
sub = rospy.Subscriber('/first_tb3/scan', LaserScan, callback)
pub = rospy.Publisher('/first_tb3/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(2)
move = Twist()

rospy.spin()