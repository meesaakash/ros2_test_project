# ros2_test_project
Showcase of a ros2 simulation robot with two wheels and able to drive around via keyboard commands (WASD) or preset publisher function.

Using ROS2 Humble on Mac M1

Next steps: Building pose estimator for simulating roaming on a complex terrain.  

# useful commands:

1. colcon build --symlink-install --packages-select my_test_rover
2. ros2 launch my_test_rover test.launch.py
3. source local_setup.sh
4. rviz2 -d my_rover.rviz
