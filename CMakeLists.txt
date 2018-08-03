cmake_minimum_required(VERSION 2.8.3)
project(pico)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  pico_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy pico_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
