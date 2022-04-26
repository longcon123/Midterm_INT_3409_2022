#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def callback(msg):
    move.angular.z = msg.angular.z
    move.linear.x = msg.linear.x + 0.1
    pub.publish(move)

rospy.init_node('run_node')
sub = rospy.Subscriber('/first_tb3/cmd_vel', Twist, callback)
pub = rospy.Publisher('/second_tb3/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(2)
move = Twist()

rospy.spin()