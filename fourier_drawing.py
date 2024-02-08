import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import turtle
import time

rad_per_index = 2*np.pi
samples_per_line = 100
RATE = 180/np.pi

# test data
inc = np.linspace(0, 20, samples_per_line)
dec = np.linspace(20, 0, samples_per_line)
zeros = np.zeros(inc.size)
high = np.ones(inc.size)*20


x = np.hstack((inc, dec, inc, dec))
y = np.hstack((inc, high, zeros, zeros))

r = np.sqrt(x**2 + y**2)
n = np.linspace(0, r.size/RATE, r.size)
print(n.size)

# print(x)
# print(y)
# print(r)

transform = fftpack.fft(r)

amplitude = np.abs(transform)[:n.size//2]
power = amplitude**2
angle = np.angle(transform)[:n.size//2]
sample_freq = fftpack.fftfreq(n.size, d=n[0]-n[1])[n.size//2:]

plt.figure()
plt.plot(sample_freq, amplitude)
plt.show()

# generate each wave
# use same n array
n = n[:n.size//2]
signals = []
for i in range(n.size):
    signals.append(amplitude[i] * np.sin(angle[i]+sample_freq[i]*2*np.pi*n))


def get_x(freq, index):
    return signals[index] * np.cos(angle[index])

def get_y(freq, index):
    return signals[index] * np.sin(angle[index])

def get_coord(index):
    x = []
    y = []
    for i in range(n.size):
        x.append(get_x(sample_freq[i], i))
        y.append(get_y(sample_freq[i], i))
    return sum(x) + sum(y)
        
        

turtle.up()
turtle.goto(0,0)
turtle.down()

turtle.tracer(0, 0)
for i in range(n.size):
    print(i)
    turtle.update()
    turtle.speed("fastest")
    comp = get_coord(i)
    print(comp)
    turtle.setpos(int(comp[0])//100, int(comp[1])//100)
turtle.update()
while (True):
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break


