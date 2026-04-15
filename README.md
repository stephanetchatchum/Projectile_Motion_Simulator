# Projectile Motion Simulator

A simple interactive Python simulator for projectile motion.

Use the sliders to adjust launch angle, initial speed, and gravity while the trajectory updates in real time.

## Features

- Interactive launch angle, speed, and gravity controls
- Real-time projectile trajectory plot
- Displays max height, range, time of flight, and landing velocity
- Simple physics-based simulation using kinematic equations

## Requirements

- Python 3.8 or newer
- `matplotlib`
- `numpy`

## Installation

Install the required packages with pip:

```powershell
pip install matplotlib numpy
```

## Usage

Run the simulator with:

```powershell
python projectile.py
```

A plot window will open with sliders below the graph. Move the sliders to change the launch conditions and watch the trajectory update immediately.

## Notes

- The simulation assumes no air resistance and a flat ground at height zero.
- Gravity is adjustable so you can explore projectile behavior on different planets or environments.
