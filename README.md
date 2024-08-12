# Robot Navigation Simulator

This project showcases an autonomous robot simulation, where the robot is tasked with identifying and interacting with specific tokens in an environment while avoiding obstacles. The simulation demonstrates key concepts in robotics such as object detection, navigation, and decision-making.

## Features

- Autonomous navigation using object detection
- Avoidance of obstacles while tracking and interacting with specific targets
- Simple and effective decision-making algorithm to control robot behavior

## Installation and Setup

The simulator requires Python 2.7 and the following libraries:

- [Pygame](http://pygame.org/)
- [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331)
- [PyYAML](https://pypi.python.org/pypi/PyYAML/)

To install the necessary libraries, use the following commands:

```bash
pip install pygame pypybox2d pyyaml
```
## Running the Simulation

To run the simulation, execute the following command:

```bash
python2 run.py mySolution.py
```

## How It Works

The robot's goal is to locate and interact with silver tokens while avoiding golden tokens in the environment. The robot navigates by scanning its surroundings, identifying the location of both silver and golden tokens, and making decisions based on the detected objects.


## Pseudo-code Overview

```bash
while simulation is running:
    scan the environment for silver and golden tokens
    calculate average distances to tokens on both sides
    if a silver token is within a close range:
        move towards and interact with the silver token
    else if average distance to objects on the right > left:
        turn right
    else:
        turn left
    drive forward
```
## Environment

![image](https://user-images.githubusercontent.com/91498765/141461177-de0a459b-f97d-4fc5-b039-fb7d7638dcb8.png)

