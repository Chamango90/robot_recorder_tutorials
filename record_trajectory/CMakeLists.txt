cmake_minimum_required(VERSION 2.8.3)
project(record_trajectory)

find_package(catkin REQUIRED)
catkin_package()
catkin_python_setup()


catkin_install_python(PROGRAMS scripts/execute
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch urdf 
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})