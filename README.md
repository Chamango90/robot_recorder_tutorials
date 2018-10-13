# Tutorials for RecordIt

[![Build Status](https://travis-ci.org/ipa-jfh/robot_recorder_tutorials.svg?branch=master)](https://travis-ci.org/ipa-jfh/robot_recorder_tutorials)


## Related packages
- RecordIt: https://github.com/ipa-jfh/robot_recorder
- urdf-loader: https://github.com/gkjohnson/urdf-loaders
- urdf-animation: https://github.com/ipa-jfh/urdf-animation

## 1. record_trajectory
### Result
<a href="https://ipa-jfh.github.io/urdf-animation/manipulator_ur5/">
    <img src="https://user-images.githubusercontent.com/17281534/46701301-8f98ac00-cc1f-11e8-8ee1-af82548453d2.gif" width="249" height="211" >
</a>

[>> See 3D animation](https://ipa-jfh.github.io/urdf-animation/manipulator_ur5/)

### How to

1. Install example

    ```bash
    # Optionally create a new ROS workspace
    mkdir -p ~/record_ws/src && cd ~/record_ws/src

    # Download repositories
    git clone https://github.com/ipa-jfh/robot_recorder_tutorial.git
    wstool init .
    wstool merge ~/record_ws/src/robot_recorder_tutorial.rosinstall
    wstool up

    # Build workspace
    source /opt/ros/kinetic/setup.bash
    rosdep update && rosdep install --from-paths ~/record_ws/src --ignore-src
    cd catkin build 
    source ~/record_ws/devel/setup.bash
    ```
1. Record example

    `(auto)`
    ```bash
    roslaunch robot_recorder_example demo.launch 
    # Open another terminal
    rosrun robot_recorder_example and_action.py _record:=True
    ```
    or  
    `(manual - with RViz plugin)`  
    TODO
1. Create 3d web animation

    Follow _Create new page for your animation_ of https://github.com/ipa-jfh/urdf-animation
1. Create GIF

    Press _Record recording_ at control-box in upper right corner.  
    Set _quality_ (lower is better) and _speed_ and then press _record()_.  
    Done.  




