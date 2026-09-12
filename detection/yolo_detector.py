import numpy as np

class YOLODetector:
    def __init__(self):
        # In a real scenario, ultralytics YOLO model would be loaded here.
        # self.model = YOLO('yolo11n.pt')
        pass
        
    def get_simulated_frame(self):
        """Returns a dummy black frame for the pipeline structure."""
        return np.zeros((480, 640, 3), dtype=np.uint8)
        
    def detect(self, frame):
        """Simulates YOLOv11 detections in the frame."""
        # Returns dummy bounding boxes [x1, y1, x2, y2, conf, cls]
        return [
            {'bbox': [100, 100, 150, 150], 'conf': 0.95, 'class': 'drone'},
            {'bbox': [300, 200, 350, 250], 'conf': 0.88, 'class': 'airplane'}
        ]
