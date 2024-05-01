#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.publish_twist)

    def publish_twist(self):
        twist_msg = Twist()
        # Set linear and angular components of the Twist message
        twist_msg.linear.x = 0.2  # Example linear velocity
        twist_msg.angular.z = -0.2  # Example angular velocity
        self.publisher_.publish(twist_msg)
        self.get_logger().info('Publishing Twist command: Linear=%.2f, Angular=%.2f' % (twist_msg.linear.x, twist_msg.angular.z))

def main(args=None):
    rclpy.init(args=args)

    twist_publisher = TwistPublisher()

    rclpy.spin(twist_publisher)

    twist_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
