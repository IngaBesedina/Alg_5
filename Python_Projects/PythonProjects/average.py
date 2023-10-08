import timeit as ti
import numpy as np
import matplotlib.pyplot as plt


def bubble_sort(n, arr):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


N = 400
k = 30
x = np.array(range(10, N + 1, 10))

t = []
E = []
q = []

for n in range(10, N + 1, 10):
    a = np.array(np.random.randint(-100, 100, n))
    for i in range(30):
        start_time = ti.default_timer()
        bubble_sort(n, a)
        end_time = ti.default_timer() - start_time
        t.append(end_time)
    E.append(1/k*np.sum(t))
    q.append(np.std(t))


c = np.polyfit(x, E, 3)
f = np.poly1d(c)
x_new = np.linspace(x.min(), x.max(), 200)
y_new = f(x_new)

plt.plot(x_new, y_new, label='Fitted data', color='r')
plt.errorbar(x, E, yerr=q, fmt='o', markersize=2, capsize=2)
plt.show()
