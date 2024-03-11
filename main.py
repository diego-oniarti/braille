import math

import drawille as draw
import time
import os
import numpy as np

c = draw.Canvas()
points = [
    np.array([0, 0, 0]),
    np.array([0, 0, 1]),
    np.array([0, 1, 1]),
    np.array([0, 1, 0]),
    np.array([1, 0, 0]),
    np.array([1, 0, 1]),
    np.array([1, 1, 1]),
    np.array([1, 1, 0]),
]
points = [np.add(x, np.array([-0.5, -0.5, -0.5])) for x in points]
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


while True:
    os.system('cls')
    c.clear()

    A = math.pi / 100
    points = map(lambda punto:
                 np.matmul(punto, np.array([
                     [np.cos(A), 0, np.sin(A)],
                     [0, 1, 0],
                     [-np.sin(A), 0, np.cos(A)]
                 ])),
                 points)

    A = math.pi / 80
    points = list(map(lambda punto:
                      np.matmul(punto, np.array([
                          [np.cos(A), np.sin(A), 0],
                          [-np.sin(A), np.cos(A), 0],
                          [0, 0, 1],
                      ])),
                      points))


    def a(punto):
        b = np.add(punto, np.array([0, 0, 3]))
        return np.array([b[0], b[1], b[2], 1])

    punti_dist = list(map(a,points))

    fov = math.pi/3
    n=1
    f=10
    S = 1/np.tan(fov/2)

    def proj(p):
        return np.matmul(p, np.array([
                              [S, 0, 0, 0],
                              [0, S, 0, 0],
                              [0, 0, -f / ( f - n ) , -1],
                              [0, 0, -f*n/(f-n), 0]
                          ]))

    punti_proj = list(map(proj,punti_dist))

    for face in faces:
        for i in range(0, len(face)):
            a = punti_proj[face[i]]
            b = punti_proj[face[(i + 1) % len(face)]]

            draw_line(a[0]/a[3]*50, a[1]/a[3]*50, b[0]/b[3]*50, b[1]/b[3]*50)

    print(c.frame(-30, -30))

    time.sleep(0.05)
