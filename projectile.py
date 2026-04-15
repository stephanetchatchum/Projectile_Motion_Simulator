import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# ============================================================================
# SETUP: Initial values and figure
# ============================================================================

angle_deg = 45
speed = 20
g = 9.8

# Create figure and main axes
fig, ax = plt.subplots(figsize=(10,6))
plt.subplots_adjust(left=0.2, bottom=0.4)

# ============================================================================
# SLIDERS: User controls for angle, speed, gravity
# ============================================================================

ax_angle = plt.axes([0.2, 0.25, 0.7, 0.03])
ax_speed = plt.axes([0.2, 0.20, 0.7, 0.03])
ax_gravity = plt.axes([0.2, 0.15, 0.7, 0.03])

slider_angle = Slider(ax_angle, 'Angle(°)', 0, 90, valinit=45)
slider_speed = Slider(ax_speed, 'Speed (m/s)', 1, 100, valinit=20)
slider_gravity = Slider(ax_gravity, 'Gravity (m/s²)', 1, 20, valinit=9.8)

# ============================================================================
# PLOT OBJECTS: Create empty line and scatter objects (data filled in update)
# ============================================================================

text_box = ax.text(0.02, 0.95, '', transform=ax.transAxes, verticalalignment='top', fontsize=8)

line, = ax.plot([],[], 'b-', linewidth=2)  # Trajectory curve
scatter = ax.scatter([], [], color='red', s=100)  # Landing point

# ============================================================================
# AXES SETUP: Fixed limits and labels (so they don't scale during updates)
# ============================================================================

ax.set_xlim(0, 150)
ax.set_ylim(0, 80)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.grid(True)

# ============================================================================
# UPDATE FUNCTION: Called when any slider changes
# ============================================================================

def update(val):
    # Get current slider values
    angle_deg = slider_angle.val
    speed = slider_speed.val
    g = slider_gravity.val

    # Convert angle from degrees to radians (needed for sin/cos)
    angle_rad = math.radians(angle_deg)

    # Calculate initial velocity components (decompose into x and y)
    Ux = speed * math.cos(angle_rad)
    Uy = speed * math.sin(angle_rad)

    # Time step for simulation (smaller = more points, smoother curve)
    dt = 0.01

    # Lists to store all positions and velocities
    times = []
    Xs = []
    Ys = []
    VXs = []
    VYs = []

    # Starting position and time
    x = 0
    y = 0
    t = 0

    # ========================================================================
    # SIMULATION LOOP: Calculate trajectory until projectile hits ground
    # ========================================================================

    while y >= 0:
        # Kinematic equations: x(t) and y(t) at time t
        x = Ux * t
        y = Uy * t - 0.5 * g * t**2
        t += dt

        # Store this position and velocity
        times.append(t)
        Xs.append(x)
        Ys.append(y)
        VXs.append(Ux)  # Horizontal velocity (constant, no air resistance)
        VYs.append(Uy - g * t)  # Vertical velocity (changes due to gravity)

    # ========================================================================
    # CALCULATE STATS: Extract interesting metrics from trajectory
    # ========================================================================

    max_height = max(Ys)
    range = Xs[-1]  # Final x position (how far it went)
    time_of_flight = times[-1]  # Total time in air
    final_Vy = Uy - g * time_of_flight  # Vertical velocity when landing

    # ========================================================================
    # DISPLAY STATS: Update text box with current values
    # ========================================================================

    text = f"Angle: {angle_deg}°\n"
    text += f"Initial Speed: {speed} m/s\n"
    text += f"Max Height: {max_height:.2f} m\n"
    text += f"Range: {range:.2f} m\n"
    text += f"Time to Land: {time_of_flight:.2f} s\n"
    text += f"Final Velocity Y: {final_Vy:.2f} m/s\n"

    text_box.set_text(text)

    # ========================================================================
    # UPDATE PLOT OBJECTS: Draw trajectory and landing point
    # ========================================================================

    line.set_data(Xs, Ys)  # Update trajectory line with new data
    scatter.set_offsets(np.column_stack((Xs[-1], 0)))  # Update landing point
    fig.canvas.draw_idle()  # Redraw (efficient update, not full clear)

# ============================================================================
# CONNECT SLIDERS: Call update() whenever a slider moves
# ============================================================================

slider_angle.on_changed(update)
slider_speed.on_changed(update)
slider_gravity.on_changed(update)

# ============================================================================
# RUN
# ============================================================================

plt.show()