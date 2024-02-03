import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Графічне представлення
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
N = 10000
random_points_x = np.random.uniform(a, b, N)
random_points_y = np.random.uniform(0, f(b), N)
points_under_curve = np.sum(random_points_y < f(random_points_x))
area_under_curve = points_under_curve / N * (b - a) * f(b)

# Точне обчислення інтегралу
exact_integral, _ = spi.quad(f, a, b)

print(f"Значення інтегралу методом Монте-Карло: {area_under_curve}")
print(f"Точне значення інтегралу: {exact_integral}")
