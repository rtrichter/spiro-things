import turtle
import numpy as np
import time
screen = turtle.Screen()

increment = 2*np.pi/36000
n_increments = 1000000
center_x = 0
center_y = 0

# radii = np.array((100, 82, 28, 6), dtype=float)
# angles = np.array((0, 0, 0, 0), dtype=float)
# radii = np.array((21, 40), dtype=float)
# angles = np.array((0, 0), dtype=float)
radii = np.array((100, 22), dtype=float)
angles = np.array((0, 0), dtype=float)

def get_x(radii, angles):
    xn = radii * np.cos(angles)
    return sum(xn)

def get_y(radii, angles):
    yn = radii * np.sin(angles)
    return sum(yn)

def inc(radii, angles):
    angles[0] += increment;
    for i in range(1, radii.size):
        angles[i] += increment * radii[i-1] / radii[i]
        

print(get_x(radii, angles))
print(get_y(radii, angles))

turtle.up()
turtle.goto(center_x +get_x(radii, angles), center_y)
turtle.down()

turtle.tracer(0, 0)
for i in range(n_increments):
    if not i % 10000:
        print(i)
        turtle.update()
    turtle.speed("fastest")
    turtle.setpos(center_x + get_x(radii, angles), center_y + get_y(radii, angles))
    inc(radii, angles)
    # print(radii)
    # print(angles)
    # print()
turtle.update()
while (True):
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break