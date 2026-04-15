import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

angle_deg = 45
speed = 20
g = 9.8


fig, ax = plt.subplots(figsize=(10,6))
plt.subplots_adjust(left=0.2, bottom=0.4)

ax_angle = plt.axes([0.2, 0.25, 0.7, 0.03])
ax_speed = plt.axes([0.2, 0.20, 0.7, 0.03])
ax_gravity = plt.axes([0.2, 0.15, 0.7, 0.03])

slider_angle = Slider(ax_angle, 'Angle(°)', 0, 90, valinit=45)
slider_speed = Slider(ax_speed, 'Speed (m/s)', 1, 100, valinit=20)
slider_gravity = Slider(ax_gravity, 'Gravity (m/s²)', 1, 20, valinit=9.8)

text_box = ax.text(0.02, 0.95, '', transform=ax.transAxes, verticalalignment='top', fontsize=8)

line, = ax.plot([],[], 'b-', linewidth=2)
scatter = ax.scatter([], [], color='red', s=100)
ax.set_xlim(0,150)
ax.set_ylim(0, 80)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.grid(True)
def update(val):
    angle_deg = slider_angle.val
    speed = slider_speed.val
    g = slider_gravity.val

    angle_rad = math.radians(angle_deg)

    Ux = speed * math.cos(angle_rad)
    Uy = speed * math.sin(angle_rad)

    dt = 0.01

    times = []
    Xs = []
    Ys = []
    VXs = []
    VYs = []

    x = 0
    y = 0
    t = 0

    while y >= 0:
        x = Ux*t
        y = Uy*t - 0.5*g*t**2
        t +=dt

        times.append(t)
        Xs.append(x)
        Ys.append(y)
        VXs.append(Ux)
        VYs.append(Uy - g*t)

    max_height = max(Ys)
    range = Xs[-1]
    time_of_flight = times[-1]
    final_Vy = Uy -g*time_of_flight

    text = f"Angle: {angle_deg}°\n"
    text += f"Initial Speed: {speed} m/s\n"
    text += f"Max Height: {max_height:.2f} m\n"
    text += f"Range: {range:.2f} m\n"
    text += f"Time to Land: {time_of_flight:.2f} s\n"
    text += f"Final Velocity Y: {final_Vy:.2f} m/s\n"

    text_box.set_text(text)

    
    line.set_data(Xs, Ys)
    scatter.set_offsets(np.column_stack((Xs[-1], 0)))
    fig.canvas.draw_idle()

slider_angle.on_changed(update)
slider_speed.on_changed(update)
slider_gravity.on_changed(update)

plt.show()