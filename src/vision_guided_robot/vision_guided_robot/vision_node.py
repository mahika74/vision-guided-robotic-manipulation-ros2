import cv2
import rclpy
from pathlib import Path
from rclpy.node import Node


class VisionNode(Node):

    def __init__(self):
        super().__init__("vision_node")

        self.get_logger().info("Opening video...")

        video_path = Path.home() / "vision-guided-robotic-manipulation-ros2" / "videos" / "test.mp4"

        self.get_logger().info(f"Video path: {video_path}")

        self.cap = cv2.VideoCapture(str(video_path))

        if not self.cap.isOpened():
            self.get_logger().error(f"Failed to open video: {video_path}")
            return

        self.timer = self.create_timer(1 / 30.0, self.process_frame)

    def process_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().info("Video finished.")
            rclpy.shutdown()
            return

        cv2.imshow("Robot Camera", frame)
        cv2.waitKey(1)

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = VisionNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()