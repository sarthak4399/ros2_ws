#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtelControllerNode(Node):
    
    def __init__(self):
        super().__init__('my_robot_controller')
        self.pose_subscriber = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_vel_pub = self.create_publisher(
            Twist, 'turtle1/cmd_vel', 10)
        self.get_logger().info('My Robot Controller has been started')

    def pose_callback(self, msg: Pose):
        cmd = Twist()
        cmd.linear.x = 1.0
        cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = TurtelControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
