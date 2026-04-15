import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
beta = 0.3
gamma = 0.05

# 1. Create 100x100 grid, all zeros (susceptible = 0, infected = 1, recovered = 2)
# 2. Pick a random starting point and set it to infected (1)
# 3. For each of 100 time steps:
#    a. Find all infected cells using np.where()
#    b. For each infected cell, loop over its 8 neighbours
#       - Skip neighbours outside grid boundaries (edge cases)
#       - If neighbour is susceptible (0), infect with probability beta
#    c. For each infected cell, recover with probability gamma (set to 2)
#       - Use a copy of the grid to avoid updating while iterating
#    d. Plot the grid at selected time points (0, 10, 50, 100)

# Initialise population grid
population = np.zeros((100, 100))

# Random outbreak location
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# (Updated) Create a list for recording every frame.
history=[]

# Plot selected time points
plot_times = {0, 10, 50, 100}
fig_count = 1

# Time course: 100 time points
for t in range(101):
    
    # (Updated) Record current data.
    history.append(population.copy())
    
    if t in plot_times:
        plt.figure(figsize=(4, 5), dpi=100)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR - time {t}')
        plt.colorbar(label='0=S, 1=I, 2=R')
        plt.tight_layout()
        plt.savefig(f'patial_SIR_t{t}.png')
        plt.show()

    if t == 100:
        break

    # Work on a copy so updates don't affect current step
    new_population = population.copy()

    # Find infected cells
    infected_coords = np.array(np.where(population == 1)).T  # shape (n, 2)

    for (row, col) in infected_coords:
        # Try to recover
        recovers = np.random.choice([1, 0], p=[gamma, 1 - gamma])
        if recovers:
            new_population[row, col] = 2
            continue

        # Infect 8 neighbours
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                # Boundary check
                if 0 <= nr < 100 and 0 <= nc < 100:
                    if population[nr, nc] == 0:  # only infect susceptible
                        gets_infected = np.random.choice([1, 0], p=[beta, 1 - beta])
                        if gets_infected:
                            new_population[nr, nc] = 1

    population = new_population
    
# Create an animation to visually show the continuous change#########
print('Plz wait a moment, the animation is generating...')
# (Updated) Generate the image through 'history' list
# Another for animation
fig_anim, ax_anim = plt.subplots(figsize=(5, 5), dpi=100)

# Initialise the first frame
im_anim = ax_anim.imshow(history[0], cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
plt.colorbar(im_anim, ax=ax_anim, label='0=S, 1=I, 2=R')

# Define the animation function
def update_anim(frame):
    im_anim.set_array(history[frame])
    ax_anim.set_title(f'Spatial SIR - time {frame}')
    return [im_anim]

# Generate the animation and save
ani = animation.FuncAnimation(fig_anim, update_anim, frames=len(history), interval=100, blit=False)
ani.save('spatial_SIR.gif', writer='pillow')
plt.close(fig_anim)
print("spatial_SIR.gif is generated.")