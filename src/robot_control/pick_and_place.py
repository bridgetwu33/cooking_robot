def pick_and_place(move_group):
    # Define pick pose
    pick_pose = geometry_msgs.msg.Pose()
    pick_pose.orientation.w = 1.0
    pick_pose.position.x = 0.4
    pick_pose.position.y = 0.1
    pick_pose.position.z = 0.2

    move_group.set_pose_target(pick_pose)
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    # Simulate gripper close (not implemented)
    rospy.sleep(1)

    # Define place pose
    place_pose = geometry_msgs.msg.Pose()
    place_pose.orientation.w = 1.0
    place_pose.position.x = 0.6
    place_pose.position.y = -0.2
    place_pose.position.z = 0.2

    move_group.set_pose_target(place_pose)
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    # Simulate gripper open (not implemented)
    rospy.sleep(1)

pick_and_place(move_group)
