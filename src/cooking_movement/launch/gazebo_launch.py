from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        ),
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
