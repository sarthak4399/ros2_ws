
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from  geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__('draw_circle')
        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.send_Velocity_command)

    def send_Velocity_command(self):
        msg = Twist()
        msg.linear.x = 4.0
        msg.angular.z = 5.8
        msg.linear.y = 0.9
        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()


