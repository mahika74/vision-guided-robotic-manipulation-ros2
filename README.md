# 🤖 Vision-Guided Robotic Manipulation using State-Based Control in ROS2

> An autonomous robotic manipulation system that integrates Computer Vision, ROS2, Inverse Kinematics, and State-Based Control to perform intelligent pick-and-place operations in a simulation-first environment.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ROS2](https://img.shields.io/badge/ROS2-Humble-black)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Gazebo](https://img.shields.io/badge/Gazebo-Simulation-orange)
![RViz](https://img.shields.io/badge/RViz-Visualization-red)
![MIT License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

This project presents an autonomous vision-guided robotic manipulation system capable of detecting, localizing, and manipulating objects using a state-based control architecture in ROS2.

The system combines computer vision, robotic motion planning, inverse kinematics, and Arduino-based motor control to execute intelligent pick-and-place tasks. It follows a **simulation-first development approach**, enabling complete validation in Gazebo and RViz before deployment to physical hardware.

---

# ✨ Features

- 🎯 Real-time object detection using YOLOv8 / OpenCV
- 🤖 Autonomous pick-and-place operations
- 🧠 State-based robot control architecture
- 📐 Inverse kinematics for robotic arm motion planning
- 📡 ROS2 modular communication between nodes
- 🛠 Arduino-based motor control via serial communication
- 🧩 URDF robot modeling and visualization
- 🌍 Gazebo simulation
- 📊 RViz visualization

---

# 🏗 System Architecture

```text
Camera
   │
   ▼
Vision Node
(Object Detection)
   │
   ▼
Task Planner
(State Machine)
   │
   ▼
Inverse Kinematics
(Motion Planning)
   │
   ▼
Arduino Bridge
(Motor Controller)
   │
   ▼
Robotic Arm
```

The modular architecture separates perception, planning, kinematics, and hardware control, making the system scalable and maintainable.

---

# 🔄 Project Workflow

```text
Camera
      │
      ▼
Image Acquisition
      │
      ▼
Object Detection (YOLOv8)
      │
      ▼
Object Localization
      │
      ▼
State-Based Decision Making
      │
      ▼
Task Planner
      │
      ▼
Inverse Kinematics
      │
      ▼
Joint Command Generation
      │
      ▼
Arduino Bridge
      │
      ▼
Robotic Arm Motion
      │
      ▼
Pick-and-Place Operation
```

---

# 💻 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Robotics Framework | ROS2 |
| Computer Vision | YOLOv8, OpenCV |
| Robot Modeling | URDF |
| Simulation | Gazebo |
| Visualization | RViz |
| Motion Planning | Inverse Kinematics |
| Hardware | Arduino, Servo/DC Motors |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
vision-guided-robotic-manipulation-ros2/
│
├── diagrams/
├── docs/
├── gazebo/
├── images/
├── rviz/
├── urdf/
├── videos/
│
├── src/
│   ├── vision/
│   │   └── vision_node.py
│   ├── planner/
│   │   └── task_planner.py
│   ├── ik/
│   │   └── ik_node.py
│   ├── controller/
│   │   └── arduino_bridge.py
│   └── launch/
│       └── demo.launch.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/mahika74/vision-guided-robotic-manipulation-ros2.git
```

```bash
cd vision-guided-robotic-manipulation-ros2
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Launch the ROS2 application:

```bash
ros2 launch launch/demo.launch.py
```

Run individual modules:

### Vision Node

```bash
python src/vision/vision_node.py
```

### Task Planner

```bash
python src/planner/task_planner.py
```

### Inverse Kinematics

```bash
python src/ik/ik_node.py
```

### Arduino Bridge

```bash
python src/controller/arduino_bridge.py
```

---

# 📸 Results

## Achievements

- ✅ Real-time object detection
- ✅ Object localization
- ✅ State-based decision making
- ✅ Autonomous pick-and-place workflow
- ✅ ROS2 communication
- ✅ Simulation-first validation
- ✅ Arduino hardware integration

> Screenshots and demo videos will be added after implementation.

---

# 🎯 Applications

- Industrial Automation
- Warehouse Robotics
- Smart Manufacturing
- Material Handling
- Pick-and-Place Systems
- Robotics Research
- Educational Robotics

---

# 🔮 Future Enhancements

- YOLOv8 segmentation
- RGB-D camera support
- Multi-object grasping
- Reinforcement Learning
- Collision avoidance
- MoveIt2 integration
- Voice-controlled commands
- Cloud monitoring dashboard

---

# 👩‍💻 Author

**Mahika Bommana**

B.Tech Computer Science (AI & ML)

GitHub: https://github.com/mahika74

LinkedIn: https://www.linkedin.com/in/mahikabommana/

---
