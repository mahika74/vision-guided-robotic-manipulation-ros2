import json
import math

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class IKNode(Node):

    def __init__(self):
        super().__init__("ik_node")

        self.subscription = self.create_subscription(
            String,
            "/robot_target",
            self.target_callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            "/joint_angles",
            10
        )

        # Robot link lengths (meters)
        self.L1 = 0.20
        self.L2 = 0.20

        self.get_logger().info("IK Node Started")

    def target_callback(self, msg):

        target = json.loads(msg.data)

        x = target["x"] * 0.20
        y = target["y"] * 0.20

        r = math.sqrt(x * x + y * y)

        if r > (self.L1 + self.L2):
            self.get_logger().warning("Target out of reach")
            return

        cos_theta2 = (
            x * x + y * y - self.L1**2 - self.L2**2
        ) / (2 * self.L1 * self.L2)

        cos_theta2 = max(-1.0, min(1.0, cos_theta2))

        theta2 = math.acos(cos_theta2)

        theta1 = math.atan2(y, x) - math.atan2(
            self.L2 * math.sin(theta2),
            self.L1 + self.L2 * math.cos(theta2)
        )

        joints = {
            "joint1": round(math.degrees(theta1), 2),
            "joint2": round(math.degrees(theta2), 2)
        }

        out = String()
        out.data = json.dumps(joints)

        self.publisher.publish(out)

        self.get_logger().info(f"Joint Angles: {joints}")


def main(args=None):

    rclpy.init(args=args)

    node = IKNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()