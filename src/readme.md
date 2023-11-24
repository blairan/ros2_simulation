## 模擬

**1.純小車顯示於rviz2,包含tf_gui**

```
ros2 launch tkdiffbot mydiffbot.launch.py
```

**2.gazebo顯示模示並可控制移動(空世界)**

```
ros2 launch tkdiffbot gazebo.launch.py
```

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard`
```

3.雷達避障

**要先成功啟動gazebo再啟動雷達偵測節點**

```
ros2 launch tkdiffbot gazebo.launch.py
```

```
ros2 run obstacle_avoidence lidar_detect
```

4.建圖

```
ros2 launch tkdiffbot gazebo_into_world.launch.py
```

```
ros2 launch slam_toolbox online_async_launch.py
```

4-1保存地圖

```
ros2 run nav2_map_server map_saver_cli -f maps/coffee_map.yaml
```

5.導航

```
ros2 launch tkdiffbot gazebo_into_world.launch.py
```

```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/coffee_.yaml
```

6.送餐機器人demo

```
ros2 launch tkdiffbot gazebo_into_world.launch.py
```

```
ros2 run mqtt_test mqtt_go_pose
```

```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/coffee_.yaml
```
