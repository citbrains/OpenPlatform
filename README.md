# GankenKun ROS
ROS package for CIT Open Platform Robot GankenKun

## Dependencies
To simulate the robot on Gazebo, the following package is required
```
https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins
```

## Usage
To view URDF model on RViz (recommended)
```
roslaunch opr_bringup display_xacro.launch model:='$(find opr_description)/robots/ganken_kun_v1.xacro' gui:=true
```
To simulate the model on Gazebo
```
roslaunch opr_bringup ganken_kun_sim.launch
```
