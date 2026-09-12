import time
import math

def generate_targets():
    """Generates synthetic aerial targets with basic kinematics."""
    t = time.time() % 100
    
    # Target 1: Linear fast moving (Simulated Foe)
    target1 = {'id': 'T1', 'x': 50 + t*10, 'y': 100 + t*2, 'z': 5000}
    
    # Target 2: Circling (Simulated Friend)
    target2 = {'id': 'T2', 'x': 200 + 50*math.cos(t/5), 'y': 200 + 50*math.sin(t/5), 'z': 3000}
    
    return [target1, target2]
