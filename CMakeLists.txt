cmake_minimum_required(VERSION 2.8.3)
project(pico)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_srvs
  pico_srvs
)
catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy std_srvs pico_srvs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
