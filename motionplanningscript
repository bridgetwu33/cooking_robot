# ur10e_moveit_motion_planning.py
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import copy

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('ur10e_moveit_motion_planning', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    # Add an object to the scene
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "world"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.x = 0.4
    box_pose.pose.position.y = 0.2
    box_pose.pose.position.z = 0.5
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))

    rospy.sleep(2)

    # Plan to a joint goal
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 1.0
    joint_goal[1] = -1.0
    joint_goal[2] = 1.0
    joint_goal[3] = -1.0
    joint_goal[4] = 1.0
    joint_goal[5] = 0.0

    move_group.go(joint_goal, wait=True)
    move_group.stop()

    # Plan to a pose goal
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = 0.4
    pose_goal.position.y = 0.1
    pose_goal.position.z = 0.4

    move_group.set_pose_target(pose_goal)

    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    # Planning to slice action
    waypoints = []

    wpose = move_group.get_current_pose().pose
    wpose.position.z -= 0.1  # move down
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y += 0.2  # move right
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.z += 0.1  # move up
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                    waypoints,   # waypoints to follow
                                    0.01,        # eef_step
                                    0.0)         # jump_threshold

    move_group.execute(plan, wait=True)

    rospy.sleep(1)

    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()
