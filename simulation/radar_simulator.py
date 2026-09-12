import random
from simulation.target_generator import generate_targets

class RadarSimulator:
    def __init__(self):
        self.scan_rate = 1.0
        self.noise_level = 0.5
        
    def scan(self):
        """Simulates a 360-degree radar scan returning synthetic targets."""
        base_targets = generate_targets()
        
        # Add simulated noise
        noisy_targets = []
        for target in base_targets:
            noisy_x = target['x'] + random.uniform(-self.noise_level, self.noise_level)
            noisy_y = target['y'] + random.uniform(-self.noise_level, self.noise_level)
            noisy_targets.append({'id': target['id'], 'x': noisy_x, 'y': noisy_y, 'z': target['z']})
            
        return noisy_targets
