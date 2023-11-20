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
        self.timer_ = self.create_timer(0.2, self.send_cmd_vel)
        #訂閱雷達數據
        self.subscription = self.create_subscription(LaserScan, "/scan", self.get_scan_val, 40)
        self.region = {"left":[], "mid":[], "right":[]}
        self.linear_ = 0.2
    
    def get_scan_val(self, scan_data):
        self.region = {
            'left': int(min(min(scan_data.ranges[0:120]), 100)),
            'mid': int(min(min(scan_data.ranges[120:240]), 100)),
            'right': int(min(min(scan_data.ranges[240:360]), 100)),
        }
        print(f"{self.region['left']}/{self.region['mid']}/{self.region['right']}")

    def send_cmd_vel(self):
        self.vel = Twist()
        self.vel.linear.x = self.linear_
        if (self.region['left'] > 100 and self.region['mid'] > 100 and self.region['right'] > 100 ):
            self.vel.angular.z=1.57 # condition in which area is total clear
            print("forward")
        elif (self.region['left'] > 1 and self.region['mid'] > 1  and self.region['right'] < 1 ):
            self.vel.angular.z=1.57# object on right,taking  left 
            print("right")
        elif (self.region['left'] < 1 and self.region['mid'] > 1  and self.region['right'] > 1 ):
            self.vel.angular.z=-1.57# object on right,taking  left 
            print("left")
        elif (self.region['left'] < 1 and self.region['mid'] < 1  and self.region['right'] < 1 ):
            self.vel.angular.z=3.14# object ahead take full turn
            print("reverse")
        elif (self.region['left'] > 1 and self.region['mid'] < 1  and self.region['right'] < 1 ):
            self.vel.angular.z=1.57# object ahead take full turn
            print("left")
        elif (self.region['left'] > 1 and self.region['mid'] > 1  and self.region['right'] < 1 ):
            self.vel.angular.z=1.57# object ahead take full turn
            print("left")
        elif (self.region['left'] < 1 and self.region['mid'] < 1  and self.region['right'] > 1 ):
            self.vel.angular.z=1.57# object ahead take full turn
            print("right")
        


        self.cmd_vel_pub.publish(self.vel)



def main(args=None):
    rclpy.init(args=args)
    obstacle_avoid = ObstacleAvoiding()
    rclpy.spin(obstacle_avoid)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
