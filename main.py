import math

import drawille as draw
import time
import os
import numpy as np

c = draw.Canvas()
points = [
    np.array([0, 0, 0, 1]),
    np.array([0, 0, 1, 1]),
    np.array([0, 1, 1, 1]),
    np.array([0, 1, 0, 1]),
    np.array([1, 0, 0, 1]),
    np.array([1, 0, 1, 1]),
    np.array([1, 1, 1, 1]),
    np.array([1, 1, 0, 1]),
]
points = [np.add(x, np.array([-0.5, -0.5, -0.5, 0])) for x in points]
faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]


def draw_line(x1, y1, x2, y2):
    for x, y in draw.line(int(x1), int(y1), int(x2), int(y2)):
        c.set(x, y)
        # c.set(x+1, y)
        # c.set(x, y+1)


A1 = math.pi / 100
A2 = math.pi / 81
rot_mat = np.array([
    [np.cos(A1) * np.cos(A2), np.cos(A1) * np.sin(A2), np.sin(A1), 0],
    [-np.sin(A2), np.cos(A2), 0, 0],
    [-np.sin(A1) * np.cos(A2), -np.sin(A2) * np.sin(A1), np.cos(A2), 0],
    [0,0,0,0],
])

fov = math.pi / 3
n = 1
f = 10
S = 1 / np.tan(fov / 2)
proj = np.array([
        [S, 0, 0, 0],
        [0, S, 0, 0],
        [0, 0, -f / (f - n), -1],
        [0, 0, -f * n / (f - n), 0]
])

scale = 75
T=0
while True:
    c.clear()

    points = list(map(lambda punto: np.matmul(punto, rot_mat), points))
    punti_dist = list(map(lambda p: np.add(p,np.array([0, 0, 3, 0])), points))
    punti_proj = list(map(lambda p: np.matmul(p,proj), punti_dist))

    for face in faces:
        for i in range(0, len(face)):
            a = punti_proj[face[i]]
            b = punti_proj[face[(i + 1) % len(face)]]

            draw_line(a[0] / a[3] * scale, a[1] / a[3] * scale, b[0] / b[3] * scale, b[1] / b[3] * scale)

    scale = 75 + np.sin(T/10)*25

    os.system('cls')
    print(c.frame(-55, -55))

    time.sleep(0.05)
    T+=1
