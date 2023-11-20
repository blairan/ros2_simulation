import rclpy
from rclpy.node import Node
import paho.mqtt.client as mqtt

class mqtt_sub(Node):
    def __init__(self, host="192.168.93.155", port=1883, topic="ros2_hello/msg"):
        super().__init__("mqtt_sub_node")
        self.host = host
        self.port = port
        self.topic = topic
        self.count = 0
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, usrdata, flags,rc):
        print("聯接mqtt結果:{}")
        self.client.subscribe(self.topic)
    def on_message(self, client, usrdata, msg):
        self.count+=1
        word_str = msg.payload
        print(f"massage {self.count}: {msg.topic} {str(word_str, encoding='utf-8')}")
    def start(self):
        self.client.connect(self.host, self.port, 60)
        self.client.loop_forever()

    
def main(args=None):
    rclpy.init(args=args)
    mqtt = mqtt_sub()
    mqtt.start()
    rclpy.spin(mqtt_sub)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
