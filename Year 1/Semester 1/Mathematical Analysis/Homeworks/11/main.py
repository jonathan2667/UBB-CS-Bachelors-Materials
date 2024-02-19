import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the quadratic function
def f(A, x):
    return 0.5 * x.T @ A @ x

# Create a grid of points
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Define the matrices A
A_min = np.array([[2, 0], [0, 2]])
A_max = np.array([[-2, 0], [0, -2]])
A_saddle = np.array([[2, 0], [0, -2]])

# Compute the function values
Z_min = np.array([f(A_min, np.array([x,y])) for x, y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
Z_max = np.array([f(A_max, np.array([x,y])) for x, y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
Z_saddle = np.array([f(A_saddle, np.array([x,y])) for x, y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

# Compute the gradients
grad_min = np.gradient(Z_min)
grad_max = np.gradient(Z_max)
grad_saddle = np.gradient(Z_saddle)

# Create the figure
fig = plt.figure(figsize=(18, 12))

# Plot the 3D surfaces
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z_min, cmap='viridis')
ax1.set_title('Unique Minimum')

ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z_max, cmap='viridis')
ax2.set_title('Unique Maximum')

ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z_saddle, cmap='viridis')
ax3.set_title('Unique Saddle Point')

# Plot the contour lines and gradients
ax4 = fig.add_subplot(234)
ax4.contour(X, Y, Z_min, cmap='viridis')
ax4.quiver(X[::5, ::5], Y[::5, ::5], grad_min[1][::5, ::5], grad_min[0][::5, ::5])
ax4.set_title('Contour and Gradient - Unique Minimum')

ax5 = fig.add_subplot(235)
ax5.contour(X, Y, Z_max, cmap='viridis')
ax5.quiver(X[::5, ::5], Y[::5, ::5], grad_max[1][::5, ::5], grad_max[0][::5, ::5])
ax5.set_title('Contour and Gradient - Unique Maximum')

ax6 = fig.add_subplot(236)
ax6.contour(X, Y, Z_saddle, cmap='viridis')
ax6.quiver(X[::5, ::5], Y[::5, ::5], grad_saddle[1][::5, ::5], grad_saddle[0][::5, ::5])
ax6.set_title('Contour and Gradient - Unique Saddle Point')

# Add text to the plot
plt.text(0, 1, 'Mogovan Jonathan - Group 915', horizontalalignment='left', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show()