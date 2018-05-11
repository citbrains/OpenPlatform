# opr_bringup

## Overview
Open Platform Robot bring up package

## Simulation
### Rviz
```
roslaunch opr_bringup display_xacro.launch model:='$(find opr_description)/robots/ganken_kun_v1.xacro' gui:=true
```
### Gazebo
MimicJointPlugin is required to simulate robot in Gazebo
```
roslaunch opr_bringup ganken_kun_sim.launch 
```

## Real
