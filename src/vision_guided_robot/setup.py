from setuptools import find_packages, setup

package_name = 'vision_guided_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    (
        'share/ament_index/resource_index/packages',
        ['resource/' + package_name],
    ),
    (
        'share/' + package_name,
        ['package.xml'],
    ),
    (
        'share/' + package_name + '/launch',
        [
            'launch/robot_system.launch.py',
            'launch/display.launch.py',
        ],
    ),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahika',
    maintainer_email='mahika@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'vision_node = vision_guided_robot.vision_node:main',
            'task_planner = vision_guided_robot.task_planner:main',
            'coordinate_transform = vision_guided_robot.coordinate_transform:main',
            'ik_node = vision_guided_robot.ik_node:main',
            'arduino_bridge = vision_guided_robot.arduino_bridge:main',
        ],
    },
)