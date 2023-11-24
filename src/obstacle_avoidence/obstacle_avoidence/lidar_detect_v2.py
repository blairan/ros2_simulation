import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoiding(Node):
    def __init__(self):
        super().__init__("lidar_detect")
        #發布速度指令
        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", 20)
        #發布後的回呼
        # self.timer_ = self.create_timer(0.2, self.send_cmd_vel)
        #訂閱雷達數據
        self.subscription = self.create_subscription(LaserScan, "/scan", self.get_scan_val, 40)
        self.linear_ = 0.2
         # 設定閾值，假設障礙物的最小距離為0.5米
        self.obstacle_threshold = 0.5
    def get_scan_val(self, scan_data):
        for i, distance in enumerate(scan_data.ranges):
            if distance < self.obstacle_threshold:
                print(f"檢測到障礙物在角度:{scan_data.angle_min + i * scan_data.angle_increment}米, 距離 {distance} 米")
        
    
def main(args=None):
    rclpy.init(args=args)
    obstacle_avoid = ObstacleAvoiding()
    rclpy.spin(obstacle_avoid)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
