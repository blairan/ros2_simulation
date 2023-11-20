from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command,LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_name = "tkdiffbot"
    # mydiffbot_scription = FindPackageShare(package=pkg_name).find(pkg_name)
    # urdf_mode = os.path.join(mydiffbot_scription, "urdf", "tkbot_model.urdf")
    mydiffbot_scription = get_package_share_directory("tkdiffbot")
    
    urdf_mode = os.path.join(mydiffbot_scription, "urdf", "tkbot_model.urdf.xacro")
    rviz_config = os.path.join(mydiffbot_scription, "rviz", "deflaut_rviz")
    model = DeclareLaunchArgument(name="model", default_value=urdf_mode)
    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]))
    # 加載機器人模型
    #1.啟動robot_state_publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        # arguments=[urdf_mode]
        parameters=[{"robot_description":robot_description}]
    )
    #2.啟動joint_state_publisher
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
    )

    #3.啟動joint_state_publisher_gui用以生成tf
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    #4.rviz2顯示模型
    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=[rviz_config]
    )
    
    return LaunchDescription([
        model,
        robot_state_publisher,
        joint_state_publisher,
        joint_state_publisher_gui,
        rviz2,
    ])