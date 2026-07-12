import cv2
import json
import rclpy
from pathlib import Path
from rclpy.node import Node
from std_msgs.msg import String
from ultralytics import YOLO


class VisionNode(Node):

    def __init__(self):
        super().__init__("vision_node")

        # Load YOLO model
        self.get_logger().info("Loading YOLOv8 model...")
        self.model = YOLO("yolov8n.pt")
        self.get_logger().info("YOLO model loaded successfully.")

        # ROS2 Publisher
        self.publisher = self.create_publisher(
            String,
            "/object_detection",
            10
        )

        # Open video
        self.get_logger().info("Opening video...")

        video_path = (
            Path.home()
            / "vision-guided-robotic-manipulation-ros2"
            / "videos"
            / "test.mp4"
        )

        self.get_logger().info(f"Video path: {video_path}")

        self.cap = cv2.VideoCapture(str(video_path))

        if not self.cap.isOpened():
            self.get_logger().error(f"Failed to open video: {video_path}")
            return

        self.timer = self.create_timer(
            1.0 / 30.0,
            self.process_frame
        )

    def process_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().info("Video finished.")
            rclpy.shutdown()
            return

        # Run YOLO inference
        results = self.model(frame)

        # Draw bounding boxes
        annotated_frame = results[0].plot()

        # Publish first detected object
        if len(results[0].boxes) > 0:

            box = results[0].boxes[0]

            cls = int(box.cls[0])
            label = self.model.names[cls]

            x1, y1, x2, y2 = box.xyxy[0]

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            confidence = float(box.conf[0])

            message = {
                "class": label,
                "x": center_x,
                "y": center_y,
                "confidence": round(confidence, 2)
            }

            msg = String()
            msg.data = json.dumps(message)

            self.publisher.publish(msg)

        cv2.imshow("Robot Camera", annotated_frame)
        cv2.waitKey(1)

    def destroy_node(self):
        if hasattr(self, "cap"):
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
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()