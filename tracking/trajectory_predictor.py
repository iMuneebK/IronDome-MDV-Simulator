from tracking.kalman_filter import KalmanFilter
import numpy as np

class TrajectoryPredictor:
    def __init__(self):
        self.trackers = {}
        
    def predict_future_position(self, target_id, current_x, current_y, steps=10):
        """Predict future trajectory using Kalman Filter."""
        if target_id not in self.trackers:
            self.trackers[target_id] = KalmanFilter()
            # Initialize with first measurement
            self.trackers[target_id].x[0] = current_x
            self.trackers[target_id].x[1] = current_y
            
        kf = self.trackers[target_id]
        
        # Update with current measurement
        z = np.array([[current_x], [current_y]])
        kf.update(z)
        
        # Predict future states
        temp_x = np.copy(kf.x)
        temp_P = np.copy(kf.P)
        
        future_positions = []
        for _ in range(steps):
            pred = kf.predict()
            future_positions.append((float(pred[0]), float(pred[1])))
            
        # Restore state
        kf.x = temp_x
        kf.P = temp_P
        
        return future_positions
