import timeit as ti
import numpy as np
import statistics
import matplotlib.pyplot as plt

mysetup = """
from __main__ import n
from __main__ import a
from __main__ import bubble_sort
"""


def bubble_sort(n, arr):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


N = 400
x = np.array(range(10, N + 1, 10))
y = []

for n in range(10, N+1, 10):
    a = np.array(np.random.randint(-100, 100, n))
    a[::-1].sort()
    y.append(ti.timeit(setup=mysetup, stmt="bubble_sort(n, a)", number=10))

print("Коэффициент корреляции:", statistics.correlation(x, y))
model = np.poly1d(np.polyfit(x, y, 2))
x_new = np.linspace(x.min(), x.max(), 200)
y_new = model(x_new)
print("Уравнение кривой:")
print(model)
plt.scatter(x, y, s=7, color='b')
plt.plot(x_new, y_new, color='r')
plt.xlabel('Размер массива')
plt.ylabel('Время работы функции')
plt.title('Худший случай')
plt.show()
