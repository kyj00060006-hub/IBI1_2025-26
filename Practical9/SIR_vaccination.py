import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

beta = 0.3
gamma = 0.05
N = 10000
vaccination_rates = [i / 10 for i in range(11)]  # 0%, 10%, ..., 100%

plt.figure(figsize=(8, 5), dpi=150)

for idx, vac_rate in enumerate(vaccination_rates):
    vaccinated = int(N * vac_rate)
    I = 1
    S = N - vaccinated - I
    R = vaccinated  # vaccinated individuals treated as immune (recovered)

    I_list = [I]

    for t in range(1000):
        if S <= 0 or I <= 0:
            I_list.append(I)
            continue

        p_infect = beta * (I / N)
        new_infections = np.sum(np.random.choice([1, 0], S, p=[p_infect, 1 - p_infect]))
        new_recoveries = np.sum(np.random.choice([1, 0], I, p=[gamma, 1 - gamma]))

        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R = R + new_recoveries

        I_list.append(I)

    color = cm.viridis(idx / len(vaccination_rates))
    label = f'{int(vac_rate * 100)}%'
    plt.plot(I_list, color=color, label=label)

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='vaccination rate', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=7)
plt.tight_layout()
plt.savefig('SIR_vaccination_plot.png')
plt.show()