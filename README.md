# ros2_test_project
Showcase of a ros2 simulation robot with two wheels and able to drive around via published commands

Using Ros2 humble on Mac M1


useful commands:

colcon build --symlink-install --packages-select my_test_rover
ros2 launch my_test_rover test.launch.py
source local_setup.sh
rviz2 -d my_rover.rviz
