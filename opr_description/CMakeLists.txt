cmake_minimum_required(VERSION 2.8.3)
project(opr_description)

find_package(catkin REQUIRED COMPONENTS
  xacro
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

