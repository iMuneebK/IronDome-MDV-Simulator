import os

class RadarDisplay:
    def __init__(self):
        pass
        
    def update(self, tracked_objects):
        """Prints a text-based dashboard representing the visualization."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== IronDome-MDV Radar Dashboard ===")
        print("ACADEMIC PROOF-OF-CONCEPT ONLY\n")
        
        for obj in tracked_objects:
            print(f"Target {obj['id']}:")
            print(f"  Position: {obj['current_pos'][0]:.2f}, {obj['current_pos'][1]:.2f}, {obj['current_pos'][2]:.2f}")
            print(f"  Class: {obj['classification']}")
            print(f"  Threat: {obj['threat_level']}")
            if obj['threat_level'] == "FOE":
                print(f"  Intercept Point: {obj['intercept_point'][0]:.2f}, {obj['intercept_point'][1]:.2f}")
            print("-" * 30)
