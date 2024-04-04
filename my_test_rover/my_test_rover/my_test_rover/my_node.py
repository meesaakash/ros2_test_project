# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# import time

# class MoveRobotNode(Node):
#     def __init__(self):
#         super().__init__('move_robot')
#         self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
#         timer_period = 0.1  # seconds
#         self.timer = self.create_timer(timer_period, self.move_robot)
#         self.i = 0
#         self.nodeName = self.get_name()
#         self.get_logger().info("{0} started mynode move robot".format(self.nodeName))

#     def move_robot(self):
#         self.get_logger().info("... moving robot")
#         msg = Twist()
#         # Forward for 2 seconds
#         if self.i < 20:
#             msg.linear.x = 0.5
#         # Backward for 2 seconds
#         elif self.i < 40:
#             msg.linear.x = -0.5
#         # Turn for 5 seconds
#         elif self.i < 90:
#             msg.angular.z = 0.5
#         # move forward 1 sec
#         elif self.i < 100:
#             msg.linear.x = 0.5
#         else:
#             self.i = 0

#         self.publisher_.publish(msg)
#         self.i += 1

# def main(args=None):
#     rclpy.init(args=args)
#     move_robot_node = MoveRobotNode()
#     rclpy.spin(move_robot_node)
#     move_robot_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import time

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.i = 0

    def move_robot(self):
        msg = Twist()
        # Forward for 2 seconds
        if self.i < 20:
            msg.linear.x = 0.5
        # Backward for 2 seconds
        elif self.i < 40:
            msg.linear.x = -0.5
        # Turn for 5 seconds
        elif self.i < 90:
            msg.angular.z = 0.5
        # Move forward for 1 second
        elif self.i < 100:
            msg.linear.x = 0.5
        else:
            self.i = 0

        self.publisher_.publish(msg)

        # Create a TransformStamped message
        tf_msg = TransformStamped()
        tf_msg.header.stamp = self.get_clock().now().to_msg()
        tf_msg.header.frame_id = 'base_link'
        tf_msg.child_frame_id = 'base_laser'
        tf_msg.transform.translation.x = 0.1  # Example translation (x, y, z)
        tf_msg.transform.translation.y = 0.0
        tf_msg.transform.translation.z = 0.2
        tf_msg.transform.rotation.x = 0.0  # Example rotation (x, y, z, w)
        tf_msg.transform.rotation.y = 0.0
        tf_msg.transform.rotation.z = 0.0
        tf_msg.transform.rotation.w = 1.0

        # Publish the transform
        self.tf_broadcaster.sendTransform(tf_msg)

        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    move_robot_node = MoveRobotNode()
    rclpy.spin(move_robot_node)
    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
