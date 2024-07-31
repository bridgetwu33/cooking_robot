from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('rviz2'), 'launch', 'rviz2.launch.py')]),
            launch_arguments={'config': 'path/to/your/rviz/config/file.rviz'}.items(),
        ),
    ])