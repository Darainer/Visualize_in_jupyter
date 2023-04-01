import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


def plot_vehicle(pos, dim, angle, color, label):
    """Function to plot a vehicle as a rectangle."""
    rect = patches.Rectangle((pos[0], pos[1]), dim[0], dim[1], angle=angle, color=color, alpha=0.7, label=label)
    plt.gca().add_patch(rect)


import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data, vehicle_a_dim=(4.5, 1.8), vehicle_b_dim=(4.0, 1.9), fov_angle=120, fov_radius=10):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Initialize patches for both vehicles
    vehicle_a_patch = patches.Rectangle((0, 0), vehicle_a_dim[0], vehicle_a_dim[1], angle=0, color='red', label='Vehicle A')
    vehicle_b_patch = patches.Rectangle((0, 0), vehicle_b_dim[0], vehicle_b_dim[1], angle=90, color='blue', label='Vehicle B')
    
    # Initialize patch for field of view polygon
    vehicle_a_fov_patch = patches.Polygon(xy=[(0,0),(1,1),(2,2)], facecolor='gray', alpha=0.3)

    def init():
        ax.add_patch(vehicle_a_patch)
        ax.add_patch(vehicle_b_patch)
        ax.add_patch(vehicle_a_fov_patch)
        plt.xlim(-5, 50)
        plt.ylim(-5, 50)
        plt.xlabel('X-direction (m)')
        plt.ylabel('Y-direction (m)')
        plt.legend()
        plt.grid()
        return vehicle_a_patch, vehicle_b_patch, vehicle_a_fov_patch

    def update(frame):
        vehicle_a_pos = vehicle_a_data[frame]
        vehicle_b_pos = vehicle_b_data[frame]

        vehicle_a_patch.set_xy(vehicle_a_pos)
        vehicle_b_patch.set_xy(vehicle_b_pos)
        
        # Update field of view polygon vertices
        fov_center = vehicle_a_pos + np.array([vehicle_a_dim[0] / 2, vehicle_a_dim[1] / 2])
        fov_left = fov_center + fov_radius * np.array([np.cos(np.deg2rad(vehicle_a_patch.angle + fov_angle / 2)), np.sin(np.deg2rad(vehicle_a_patch.angle + fov_angle / 2))])
        fov_right = fov_center + fov_radius * np.array([np.cos(np.deg2rad(vehicle_a_patch.angle - fov_angle / 2)), np.sin(np.deg2rad(vehicle_a_patch.angle - fov_angle / 2))])
        vehicle_a_fov_patch.set_xy([fov_center, fov_left, fov_right])

        return vehicle_a_patch, vehicle_b_patch, vehicle_a_fov_patch

    animation = FuncAnimation(fig, update, frames=len(vehicle_a_data), init_func=init, blit=True)
    plt.close()
    return animation




if __name__ == '__main__':
    # Example motion data
    vehicle_a_data = np.array([[i, 0] for i in range(20)])
    vehicle_b_data = np.array([[10, i] for i in range(20)])

    visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data)
