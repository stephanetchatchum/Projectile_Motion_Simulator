import math
import matplotlib.pyplot as plt

# PART 1: Input (what the user controls)
angle_deg = 45
speed = 20
gravity = 9.8

# PART 2: Convert angle to radians
angle_rad = math.radians(angle_deg)

# PART 3: Calculate initial velocity components
Ux = speed * math.cos(angle_rad)
Uy = speed * math.sin(angle_rad)

# PART 4: Simulate (calculate all positions until ball hits ground)
# TODO: Loop and collect positions

# PART 5: Plot the trajectory
# TODO: Draw the path

# PART 6: Display stats
# TODO: Show numbers