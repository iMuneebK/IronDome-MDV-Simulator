import time
from simulation.radar_simulator import RadarSimulator
from detection.yolo_detector import YOLODetector
from fusion.sensor_fusion import SensorFusion
from visualization.radar_display import RadarDisplay

def main():
    print("Starting IronDome-MDV Simulation...")
    radar = RadarSimulator()
    detector = YOLODetector()
    fusion_engine = SensorFusion()
    display = RadarDisplay()

    try:
        while True:
            # Generate simulated radar data
            radar_data = radar.scan()
            
            # Simulate camera frame (dummy logic for simulation loop)
            camera_frame = detector.get_simulated_frame()
            
            # Detect objects in camera frame
            cv_detections = detector.detect(camera_frame)
            
            # Sensor Fusion: Combine radar and CV data
            tracked_objects = fusion_engine.fuse_and_track(radar_data, cv_detections)
            
            # Update Dashboard
            display.update(tracked_objects)
            
            time.sleep(0.1) # 10 FPS Simulation
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
