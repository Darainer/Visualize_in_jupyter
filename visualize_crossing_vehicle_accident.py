import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_vehicle(pos, dim, angle, color, label):
    """Function to plot a vehicle as a rectangle."""
    rect = patches.Rectangle((pos[0], pos[1]), dim[0], dim[1], angle=angle, color=color, alpha=0.7, label=label)
    plt.gca().add_patch(rect)

def visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data, vehicle_a_dim=(4.5, 1.8), vehicle_b_dim=(4.0, 1.9)):
    plt.figure(figsize=(10, 10))
    
    for i, (vehicle_a_pos, vehicle_b_pos) in enumerate(zip(vehicle_a_data, vehicle_b_data)):
        plt.clf()
        
        # Plot Vehicle A
        plot_vehicle(vehicle_a_pos, vehicle_a_dim, 0, 'red', 'Vehicle A')
        
        # Plot Vehicle B
        plot_vehicle(vehicle_b_pos, vehicle_b_dim, 90, 'blue', 'Vehicle B')
        
        # Set axis limits and labels
        plt.xlim(-5, 50)
        plt.ylim(-5, 50)
        plt.xlabel('X-direction (m)')
        plt.ylabel('Y-direction (m)')
        
        # Add legend and grid
        plt.legend()
        plt.grid()
        
        # Save each frame as an image
        plt.savefig(f'frame_{i:03d}.png')

if __name__ == '__main__':
    # Example motion data
    vehicle_a_data = np.array([[i, 0] for i in range(20)])
    vehicle_b_data = np.array([[10, i] for i in range(20)])

    visualize_crossing_vehicle_accident(vehicle_a_data, vehicle_b_data)
