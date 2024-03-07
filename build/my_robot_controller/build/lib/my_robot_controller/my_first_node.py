import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__('my_first_node')
        self.get_logger().info('This will not work in hazardous areas like nuclear power plants where humans cannot go.')
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello World!' + str(self.counter))
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyFirstNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    # Additional code here
