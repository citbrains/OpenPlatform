cmake_minimum_required(VERSION 2.8.3)
project(opr_gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  gazebo_ros_control
  hardware_interface
  urdf
  xacro
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

