import cv2

class CameraDisplay:
    def __init__(self):
        self.window_name = "IronDome-MDV: Tracking Feed"
        
    def render_frame(self, frame, detections):
        """Renders bounding boxes on camera frame."""
        # Simple simulation: doesn't actually run cv2.imshow in headless tests
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, det['class'], (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        return frame
