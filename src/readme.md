## 模擬

**1.純小車顯示於rviz2,包含tf_gui**

```
ros2 launch tkdiffbot mydiffbot.launch.py
```

**2.gazebo顯示模示並可控制移動**

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
