#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.get_logger().info('Subscriber node has been started')

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg.x) + ' ' + str(msg.y) + ' ' + str(msg.theta) + ' ' + str(msg.linear_velocity) + ' ' + str(msg.angular_velocity))
        self.get_logger().info('Pose has been received')
def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    try:
        rclpy.spin(node)
        print('Node has been started')
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


