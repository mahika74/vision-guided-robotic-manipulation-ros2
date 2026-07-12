from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package="vision_guided_robot",
            executable="vision_node",
            name="vision_node",
            output="screen"
        ),

        Node(
            package="vision_guided_robot",
            executable="task_planner",
            name="task_planner",
            output="screen"
        ),

        Node(
            package="vision_guided_robot",
            executable="coordinate_transform",
            name="coordinate_transform",
            output="screen"
        ),

        Node(
            package="vision_guided_robot",
            executable="ik_node",
            name="ik_node",
            output="screen"
        ),

        Node(
            package="vision_guided_robot",
            executable="arduino_bridge",
            name="arduino_bridge",
            output="screen"
        ),
    ])