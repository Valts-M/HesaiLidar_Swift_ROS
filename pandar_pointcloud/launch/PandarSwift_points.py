from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():

    share_dir = get_package_share_directory('pandar_pointcloud')

    return LaunchDescription([
        launch_ros.actions.Node(
            package ='pandar_pointcloud',
            namespace ='hesai',
            executable ='pandar_cloud_node',
            name ='pandar_pointcloud',
            output ="screen",
            parameters=[
                # {"pcap": "''"},
                {"device_ip"  : "192.168.1.201"},
                {"port"  : 2368},
                {"start_angle"  : 0.0},
                {"frame_id"  : "PandarSwift"},
                {"publish_model"  : "both_point_raw"},
                {"calibration"  : "{share_dir}/params/PandarQT128_Correction.csv"},
                {"firetime_file"  : "{share_dir}/params/PandarQT128_Firetimes.csv"},
                {"coordinate_correction_flag"  : False},
                # {"cert_file"  : "''"},
                # {"private_key_file"  : "''"},
                # {"ca_file"  : "''"},
            ]
        )
    ])
