import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

times = []
for n in range(10, 201, 10):
    arr = [random.randint(0, 1000) for _ in range(n)]
    temp_times = []
    for i in range(30):
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        temp_times.append(end_time - start_time)
    avg_time = sum(temp_times) / len(temp_times)
    deviation = ((sum((x - avg_time) ** 2 for x in temp_times)) / len(temp_times)) ** 0.5
    times.append((n, avg_time, deviation))

ns = [t[0] for t in times]
avg_times = [t[1] for t in times]
deviations = [t[2] for t in times]
print(ns)
print(avg_times)
print(deviations)

plt.errorbar(ns, avg_times, yerr=deviations, fmt='o', markersize=3, capsize=2)
plt.xlabel('Array size')
plt.ylabel('Time (s)')
plt.title('Bubble Sort Performance')
plt.show()