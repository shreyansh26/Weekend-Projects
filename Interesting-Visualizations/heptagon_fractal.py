import matplotlib.pyplot as plt
import numpy as np
import math

SIZE = 20
plt.rcParams['axes.facecolor'] = 'black'

def plot(points, heptagon_points):
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points), marker=".", color="blue")
    ax.scatter(*zip(*heptagon_points), marker="*", color="red")
    plt.xlim([-60, 60])
    plt.ylim([-60, 60])
    plt.axis('off')
    plt.show()



points_x = np.random.uniform(-50, 50, size=SIZE)
points_y = np.random.uniform(-50, 50, size=SIZE)

points = np.array(list(zip(points_x, points_y)))

ARG = (2*math.pi)/7
heptagon_points = 30*np.array([(1,0), (math.cos(ARG), math.sin(ARG)), (math.cos(ARG), -math.sin(ARG)), (math.cos(2*ARG), math.sin(2*ARG)), (math.cos(2*ARG), -math.sin(2*ARG)), (math.cos(3*ARG), math.sin(3*ARG)), (math.cos(3*ARG), -math.sin(3*ARG))])


for i in range(5):
    plot(points, heptagon_points)

    temp_points = []
    for p in points:
        newp = []
        for hp in heptagon_points:
            newp.append(0.7*hp + 0.3*p)
        temp_points.extend(newp)

    points = temp_points.copy()

