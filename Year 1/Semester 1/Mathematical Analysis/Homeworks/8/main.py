import numpy as np
import matplotlib.pyplot as plt

def p_norm(vector, p):
    return np.sum(np.abs(vector)**p)**(1/p)

num_points = 10000
points = np.random.uniform(-1, 1, (num_points, 2))
p_values = [1.25, 1.5, 3, 8]
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for i, p in enumerate(p_values):
    inside_points = [point for point in points if p_norm(point, p) <= 1]
    inside_points = np.array(inside_points)
    ax = axs[i//2, i%2]
    ax.scatter(inside_points[:, 0], inside_points[:, 1])
    ax.set_title(f'Unit ball for p={p} norm')


plt.tight_layout()
plt.show()