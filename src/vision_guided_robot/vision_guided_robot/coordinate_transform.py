import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CoordinateTransform(Node):

    def __init__(self):
        super().__init__("coordinate_transform")

        self.subscription = self.create_subscription(
            String,
            "/object_detection",
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            "/robot_target",
            10
        )

        self.get_logger().info("Coordinate Transform Node Started")

    def callback(self, msg):

        data = json.loads(msg.data)

        width = 1920
        height = 1080

        x_pixel = data["x"]
        y_pixel = data["y"]

        # Temporary normalized coordinates
        x_robot = round((x_pixel - width / 2) / (width / 2), 3)
        y_robot = round((height / 2 - y_pixel) / (height / 2), 3)
        z_robot = 0.0

        output = {
            "class": data["class"],
            "x": x_robot,
            "y": y_robot,
            "z": z_robot
        }

        out = String()
        out.data = json.dumps(output)

        self.publisher.publish(out)

        self.get_logger().info(
            f'Robot Target: {output}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = CoordinateTransform()

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