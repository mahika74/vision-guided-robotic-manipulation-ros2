import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ArduinoBridge(Node):

    def __init__(self):
        super().__init__("arduino_bridge")

        self.subscription = self.create_subscription(
            String,
            "/joint_angles",
            self.callback,
            10
        )

        self.get_logger().info("Arduino Bridge Started")

    def callback(self, msg):

        joints = json.loads(msg.data)

        command = (
            f"{joints['joint1']},"
            f"{joints['joint2']}\n"
        )

        # Later this line becomes:
        # serial.write(command.encode())

        self.get_logger().info(
            f"Sending to Arduino: {command.strip()}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = ArduinoBridge()

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