import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TaskPlanner(Node):

    def __init__(self):
        super().__init__("task_planner")

        self.state = "HOME"

        self.subscription = self.create_subscription(
            String,
            "/object_detection",
            self.object_callback,
            10
        )

        self.get_logger().info("Task Planner Started")
        self.get_logger().info(f"Current State: {self.state}")

    def object_callback(self, msg):
        data = json.loads(msg.data)

        object_name = data["class"]
        x = data["x"]
        y = data["y"]
        confidence = data["confidence"]

        if self.state == "HOME":
            self.state = "SEARCH"
            self.get_logger().info("Searching for objects...")

        if self.state == "SEARCH":
            self.state = "OBJECT_FOUND"

            self.get_logger().info(
                f"Object Found: {object_name} | "
                f"Center=({x}, {y}) | "
                f"Confidence={confidence}"
            )

            self.get_logger().info("Waiting for next action...")

    def destroy_node(self):
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = TaskPlanner()

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