from tracking.trajectory_predictor import TrajectoryPredictor
from targeting.intercept_calculator import calculate_intercept

class SensorFusion:
    def __init__(self):
        self.predictor = TrajectoryPredictor()
        
    def fuse_and_track(self, radar_data, cv_detections):
        """Fuses radar positional data with CV classification."""
        fused_objects = []
        
        for rt in radar_data:
            # In a full system, you would correlate radar and CV tracks using Hungarian algorithm or similar
            classification = "Unknown"
            if len(cv_detections) > 0:
                classification = cv_detections[0]['class'] # Dummy correlation
            
            future_traj = self.predictor.predict_future_position(rt['id'], rt['x'], rt['y'])
            intercept_point = calculate_intercept(rt['x'], rt['y'], 0, 0, 300) # Dummy intercept math
            
            # Heuristic threat assessment (Academic Proof of Concept)
            threat_level = "FRIEND" if classification == "airplane" else "FOE"
            
            fused_objects.append({
                'id': rt['id'],
                'current_pos': (rt['x'], rt['y'], rt['z']),
                'predicted_trajectory': future_traj,
                'classification': classification,
                'threat_level': threat_level,
                'intercept_point': intercept_point
            })
            
        return fused_objects
