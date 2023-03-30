import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


def plot_vehicle(pos, dim, angle, color, label):
    """Function to plot a vehicle as a rectangle."""
    rect = patches.Rectangle((pos[0], pos[1]), dim[0], dim[1], angle=angle, color=color, alpha=0.7, label=label)
    plt.gca().add_patch(rect)


def visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data, vehicle_a_dim=(4.5, 1.8), vehicle_b_dim=(4.0, 1.9)):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Initialize patches for both vehicles
    vehicle_a_patch = patches.Rectangle((0, 0), vehicle_a_dim[0], vehicle_a_dim[1], angle=0, color='red', label='Vehicle A')
    vehicle_b_patch = patches.Rectangle((0, 0), vehicle_b_dim[0], vehicle_b_dim[1], angle=90, color='blue', label='Vehicle B')

    def init():
        ax.add_patch(vehicle_a_patch)
        ax.add_patch(vehicle_b_patch)
        plt.xlim(-5, 50)
        plt.ylim(-5, 50)
        plt.xlabel('X-direction (m)')
        plt.ylabel('Y-direction (m)')
        plt.legend()
        plt.grid()
        return vehicle_a_patch, vehicle_b_patch,

    def update(frame):
        vehicle_a_pos = vehicle_a_data[frame]
        vehicle_b_pos = vehicle_b_data[frame]

        vehicle_a_patch.set_xy(vehicle_a_pos)
        vehicle_b_patch.set_xy(vehicle_b_pos)
        return vehicle_a_patch, vehicle_b_patch,

    num_frames = len(vehicle_a_data)
    ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)
    plt.close(fig)  # Prevents double display of the plot
    return ani


if __name__ == '__main__':
    # Example motion data
    vehicle_a_data = np.array([[i, 0] for i in range(20)])
    vehicle_b_data = np.array([[10, i] for i in range(20)])

    visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data)
