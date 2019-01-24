# Tutorials for RecordIt

[![Build Status](https://travis-ci.org/ipa-jfh/robot_recorder_tutorials.svg?branch=master)](https://travis-ci.org/ipa-jfh/robot_recorder_tutorials)


## Related packages
- RecordIt: https://github.com/ipa-jfh/robot_recorder
- urdf-loader: https://github.com/gkjohnson/urdf-loaders
- urdf-animation: https://github.com/ipa-jfh/urdf-animation
- get_urdf_deps: https://github.com/ipa-jfh/get_urdf_deps

## 1. record_trajectory
### Result
<a href="https://ipa-jfh.github.io/urdf-animation/manipulator_ur5/result/">
    <img src="https://user-images.githubusercontent.com/17281534/46701301-8f98ac00-cc1f-11e8-8ee1-af82548453d2.gif" width="249" height="211" >
</a>

[>> See 3D animation](https://ipa-jfh.github.io/urdf-animation/manipulator_ur5/result/)

### How to

1. __Install example__

    ```bash
    # Optionally create a new ROS workspace
    mkdir -p ~/record_ws/src && cd ~/record_ws/src

    # Download repositories
    git clone https://github.com/ipa-jfh/robot_recorder_tutorial.git
    wstool init .
    wstool merge ~/record_ws/src/robot_recorder_tutorial/.rosinstall
    wstool up

    # Build workspace
    source /opt/ros/kinetic/setup.bash
    rosdep update && rosdep install --from-paths ~/record_ws/src --ignore-src
    cd ~/record_ws && catkin build
    source ~/record_ws/devel/setup.bash
    ```
2. __Record example__

    `(auto)`
    ```bash
    roslaunch record_trajectory record_auto.launch
    ```
    or
    `(manual - with RViz plugin)`
    TODO

    Files are saved to  `~/.ros/test_animation/`


3. __Create 3d web animation__

    Make sure to download/install nodejs/npm from https://nodejs.org/en/

    ```bash
    cd ~/.ros/test_animation/
    npm install # install all deps of the npm project
    cp -r ./node_modules/urdf-animation/template/* .
    npm start
    ```

4. __Create GIF__

    In the webpage press _Record recording_ at the control-box in upper right corner.
    Set _quality_ (lower is better) and _speed_ and then press _record()_.
    Done.

5. __Publish interactive web animation__

    To publish the web animation you have to bundle the js files first:

    ```bash
    cd ~/.ros/test_animation/
    npm run build # Might show errors which should be fine
    firefox ~/.ros/test_animation/result/index.html # test
    ```

    The folder `./result` has the self-contained webpage, which you can host e.g. on [gh-pages](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/).



