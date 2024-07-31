import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from tensorflow.keras.models import load_model
import cv2
import numpy as np

class ActionRecognition(Node):
    def __init__(self):
        super().__init__('action_recognition')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()
        self.model = load_model('/path/to/your/model.h5')
        self.class_names = ['class1', 'class2', 'class3']  # replace with actual class names

    def map_action_to_movement(self, action):
        if action == 'chop':
            return 'chop_movement'  # Replace with actual movement command
        # Add other actions and their corresponding movements
        return None

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        frame_resized = cv2.resize(frame, (64, 64))
        frame_array = np.expand_dims(frame_resized, axis=0)
        predictions = self.model.predict(frame_array)
        action_index = np.argmax(predictions)
        action = self.class_names[action_index]
        movement = self.map_action_to_movement(action)
        if movement:
            self.get_logger().info(f'Executing movement: {movement}')
            # Publish the movement command (implement this)
            # For now, just log the action

def main(args=None):
    rclpy.init(args=args)
    action_recognition = ActionRecognition()
    rclpy.spin(action_recognition)
    action_recognition.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
