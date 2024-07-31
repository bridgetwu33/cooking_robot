cmake_minimum_required(VERSION 3.5)
project(cooking_movement)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(moveit_commander REQUIRED)
find_package(tf_transformations REQUIRED)
find_package(cv_bridge REQUIRED)

install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  src/cooking_movement/action_recognition.py
  src/cooking_movement/motion_planning.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
