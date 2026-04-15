import numpy as np
import matplotlib.pyplot as plt

# Initial population
N = 10000
I = 1
S = N - I
R = 0

beta = 0.3
gamma = 0.05

# Track over time
S_list = [S]
I_list = [I]
R_list = [R]

# Time course: 1000 time points
for t in range(1000):
    # Probability of a susceptible individual getting infected
    p_infect = beta * (I / N)

    # Each susceptible: infected or not
    new_infections = np.sum(np.random.choice([1, 0], S, p=[p_infect, 1 - p_infect]))

    # Each infected: recover or not
    new_recoveries = np.sum(np.random.choice([1, 0], I, p=[gamma, 1 - gamma]))

    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.tight_layout()
plt.savefig('SIR_plot.png')
plt.show()