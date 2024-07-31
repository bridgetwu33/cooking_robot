from setuptools import find_packages, setup

package_name = 'cooking_movement'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/cooking_movement.launch.py', 'launch/rviz.launch.py', 'launch/gazebo.launch.py']),
        ('share/' + package_name + '/config', ['config/robot_moveit_config.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bridgetw',
    maintainer_email='bridgetwu33@gmail.com',
    description='Cooking robot package for ROS Humble',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_recognition = cooking_movement.action_recognition:main',
            'motion_planning = cooking_movement.motion_planning:main',
        ],
    },
)
