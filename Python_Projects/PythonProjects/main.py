import timeit as ti
import numpy as np
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

c = np.polyfit(x, y, 3)
f = np.poly1d(c)
x_new = np.linspace(x.min(), x.max(), 200)
y_new = f(x_new)

plt.scatter(x, y, s=7, label='Original data', color='b')
plt.plot(x_new, y_new, label='Fitted data', color='r')
plt.xlabel('Размер массива')
plt.ylabel('Время работы функции')
plt.title('Худший случай')
plt.show()
