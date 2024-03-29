import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import turtle
import time
from dataclasses import dataclass

samples_per_line = 20

# test data
inc = np.linspace(0, 20, samples_per_line)
dec = np.linspace(20, 0, samples_per_line)
zeros = np.zeros(inc.size)
high = np.ones(inc.size)*20

x_vec = np.hstack((inc, dec, inc, dec))
y_vec = np.hstack((inc, high, dec, zeros))

x_vec = 200*np.sin(np.linspace(0, 99, 100))
y_vec = 200*np.cos(np.linspace(0, 99, 100))


# r = np.sqrt(x**2 + y**2)
n = np.linspace(0, x_vec.size-1, x_vec.size)

# plt.figure()
# plt.plot(n, x)
# plt.show()

# x_fft = fftpack.fft(x)
# y_fft = fftpack.fft(y)


@dataclass
class FFT:
    sig: np.ndarray
    domain: np.ndarray
    trans: np.ndarray
    amp: np.ndarray
    angle: np.ndarray
    freq: np.ndarray

    def __init__(self, sig, domain):
        self.sig = sig
        self.domain = domain[:domain.size//2]
        self.half_domain = domain[:domain.size//2]
        self.trans = fftpack.fft(sig)[:domain.size//2]
        # self.trans = fftpack.fft(sig)
        self.amp = np.abs(self.trans)
        self.angle = np.angle(self.trans)[:domain.size//2]
        # self.angle = np.angle(self.trans)
        self.freq = fftpack.fftfreq(domain.size//2, d=domain[0]-domain[1])
        # self.freq = fftpack.fftfreq(domain.size, d=domain[0]-domain[1])


x_fft = FFT(x_vec, n)
y_fft = FFT(y_vec, n)

# plt.figure()
# plt.plot(x_fft.freq, x_fft.amp)
# plt.show()

print(f"domain: {x_fft.domain.size}")
print(f"amp: {x_fft.amp.size}")
print(f"freq: {x_fft.freq.size}")
print(f"angle: {x_fft.angle.size}")

x = []
y = []
# for i in range(x_fft.domain.size):
#     x.append(0)
#     y.append(0)
#     for j in range(x_fft.freq.size):
#         x[i] += x_fft.amp[j] * np.sin(x_fft.freq[j] * i + x_fft.angle[j])
#         y[i] += y_fft.amp[j] * np.sin(x_fft.freq[j] * i + y_fft.angle[j])


def get_sig(amp, freq, domain, angle):
    sig = x_fft.amp * np.sin(x_fft.freq * x_fft.domain * x_fft.angle)
    return sig


x = []
y = []
BOUND = 200
for i in range(x_fft.freq.size):
    x.append(get_sig(x_fft.amp, x_fft.freq, x_fft.domain, x_fft.angle))
    y.append(get_sig(y_fft.amp, y_fft.freq, y_fft.domain, y_fft.angle))
    # y.append(y_fft.amp * np.sin(y_fft.freq * y_fft.domain * y_fft.angle))
x_coords = sum(x) / len(x)
y_coords = sum(y) / len(x)

plt.plot(x_fft.domain, x_coords)
plt.show()

x_coords *= BOUND / max(abs(x_coords))
y_coords *= BOUND / max(abs(y_coords))


# print(y)
# plt.figure()
# plt.plot(x_fft.domain, x)
# plt.show()
# plt.figure()
# plt.plot(y_fft.domain, y)
# plt.show()
# x = np.array(x)
# y = np.array(y)
#
# x *= 100 / max(abs(x))
# y *= 100 / max(abs(y))
# print(max(x))
# print(max(y))
# print(y)

turtle.up()
turtle.setpos(0, 0)
turtle.down()
# for i in range(x_vec.size):
#     turtle.setpos(x_vec[i], y_vec[i])
for i in range(len(x_coords)):
    print(f"({x_coords[i]}, {y_coords[i]})")
    turtle.setpos(x_coords[i], y_coords[i])

time.sleep(5)


exit()

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


