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
    roslaunch record_trajectory demo.launch
    # Open another terminal
    rosrun record_trajectory record
    # Find file at: ~/.ros/recording-<DATE>.json
    ```
    or  
    `(manual - with RViz plugin)`  
    TODO
1. Create 3d web animation  

    (In record_trajectory/docs_FINAL/ one can find the final files)
    ```bash
    # Download nodejs/npm from https://nodejs.org/en/
    cd ~/record_ws/src/robot_recorder_tutorials
    gedit .gitignore
    # Add if not existing in a new line "node_modules/" (without quotes) 
    cd ~/record_ws/src/robot_recorder_tutorials/record_trajectory
    mkdir docs && cd docs
    gedit package.json
    # Insert content from below
    npm install
    cp ./node_modules/animation/template/* .
    mkdir static
    cp ../node_modules/gif.js/dist/gif.worker.js .
    # Move your recorded file to this folder
    mv ~/.ros/recording-<DATE>.json static/recording.json # Hint: <Tab> the date
    # Create the urdf
    rosrun xacro xacro --inorder -o static/ur5_with_cam.urdf ../urdf/robot.xacro

    # Modify config.js
    gedit config.js
    # Add the content from below (Modifications in `config.js`)

    firefox includes.html # YOU SHOULD SEE THE WEB 3D ANIMATION!
    ```
    `package.json`:
    ```json
    {
        "name": "record_trajectory",
        "version": "1.0.0",
        "description": "Record trajectory tutorial",
        "scripts": {
            "start": "webpack-dev-server",
            "build": " webpack"
        },
        "author": "TODO",
        "license": "Apache-2.0",
        "dependencies": {
            "urdf-animation": "^0.3.0"
        },
        "devDependencies": {
            "eslintrc": "^1.0.6"
        }
    }
    ```
    Modifications in `config.js`:
    ```js

    // Change addURDF to
    vw.addURDF({
        // https://github.com/gkjohnson/urdf-loaders
        urdf: './static/ur5_with_cam.urdf',
        packagesContainingMeshes: [
            'ur_description: https://raw.githubusercontent.com/ros-industrial/universal_robot/kinetic-devel/ur_description',
            'openni_description: https://raw.githubusercontent.com/ros-drivers/openni_camera/indigo-devel/openni_description'
        ]
    });
    // ...
    // Change camera to
    vw.setCamera({
        // https://threejs.org/docs/#api/en/cameras/PerspectiveCamera
        fov: 7,
        position: [0, 2, -10]
    });
    // ...
    // Change light position to
    // position: [60, 100, 50],
    ```

1. Create GIF

    Press _Record recording_ at control-box in upper right corner.  
    Set _quality_ (lower is better) and _speed_ and then press _record()_.  
    Done.  

1. To publish the web animation you have to bundle the js files first
    ```bash
    cd ~/record_ws/src/robot_recorder_tutorials/record_trajectory/docs
    npm install webpack webpack-cli --save-dev
    npm run build # Might show errors which should be fine
    firefox index.html # test if it works
    # Now upload the docs/ folder containing at least
    # the folder static/ and the files index.html and index.bundle.js 
    # to your repo.   
    ```
    Finally [enable gh-pages](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/) for the docs folder.



