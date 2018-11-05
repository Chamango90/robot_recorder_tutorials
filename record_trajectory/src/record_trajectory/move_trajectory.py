#!/usr/bin/env python

# This is script is solely for simulation!
# Robot and RecordIt has to be launched prior to this script.

import sys
import rospy
import moveit_commander

class ManipulatorBase():
  def __init__(self, move_group):
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    self.group =  moveit_commander.MoveGroupCommander(move_group)
    self.waypoints = []
    self.wait = 0.0

  def move_to(self, joint_goal): 
    self.group.go(joint_goal, wait=True)

  def move_to_start(self): 
    self.move_to(self.waypoints[0])

  def move_trajectory(self):
    for wp in self.waypoints:
      if rospy.is_shutdown(): break
      self.move_to(wp)
      rospy.sleep(self.wait)

class Manipulator(ManipulatorBase):
  def __init__(self):
    move_group      = rospy.get_param('~move_group', 'manipulator')
    ManipulatorBase.__init__(self, move_group)
    self.wait       = rospy.get_param('~wait', 0.1)
    self.waypoints  = rospy.get_param('~waypoints', [
      [-5.1, -1.1, 0.8, -1.0, 1.5, -6.0],
      [-5.2, -1.0, 2.1, -2.5, 1.9, -5.5],
      [-4.9, -0.7, 0.8, -1.7, 1.6, -5.9]
    ])
