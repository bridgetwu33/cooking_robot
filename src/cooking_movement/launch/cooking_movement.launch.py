from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cooking_movement',
            executable='action_recognition',
            name='action_recognition'
        ),
        Node(
            package='cooking_movement',
            executable='motion_planning',
            name='motion_planning'
        ),
    ])