#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import moveit_commander
from geometry_msgs.msg import Pose

class MotionPlanning(Node):

    def __init__(self):
        super().__init__("motion_planning_node")
        moveit_commander.roscpp_initialize([])
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('arm')
    
    def execute_movement(self, movement):
        if movement == 'chop':
            pose_goal = Pose()
            pose_goal.position.x = 0.4
            pose_goal.position.y = 0.1
            pose_goal.position.z = 0.4
            pose_goal.orientation.w = 1.0
            self.group.set_pose_target(pose_goal)
            plan = self.group.go(wait=True)
            self.group.stop()
            self.group.clear_pose_targets()

def main(args=None):
    rclpy.init(args=args)
    node = MotionPlanning()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()