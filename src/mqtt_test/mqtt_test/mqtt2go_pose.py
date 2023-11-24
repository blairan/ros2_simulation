import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import paho.mqtt.client as mqtt

class MqttRosBridge(Node):

    def __init__(self, host="192.168.93.155", port=1883, topic="/mqtt_goal_pose"):
        super().__init__('mqtt_ros_bridge')
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.host = host
        self.port = port
        self.topic = topic
        # Connect to the MQTT broker
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_message = self.on_mqtt_message
        self.mqtt_client.connect(self.host, self.port, 60)
        self.mqtt_client.loop_start()

    def on_mqtt_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code "+str(rc))
        self.mqtt_client.subscribe(self.topic)
        

    def on_mqtt_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        x, y, z = map(float, payload.split(','))
        self.publish_ros_goal_pose(x, y, z)
    def publish_ros_goal_pose(self, x, y, z):
        msg = PoseStamped()
        msg.header.stamp.sec = 0
        msg.header.frame_id = 'map'
        msg.pose.position.x = x
        msg.pose.position.y = y
        msg.pose.position.z = z
        msg.pose.orientation.w = 2.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Published goal pose: x={x}, y={y}, z={z}')

def main(args=None):
    rclpy.init(args=args)
    mqtt_ros_bridge = MqttRosBridge()
    rclpy.spin(mqtt_ros_bridge)
    mqtt_ros_bridge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

