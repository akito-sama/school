#!/usr/bin/env python
# coding: utf-8
from os import sys
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("A", help="la valeur de A dans 'a = A + BV'", type=float)
parser.add_argument("B", help="la valeur de B dans 'a = A+BV'", type=float)
parser.add_argument("dt", help="la valeur du pas dans la methode d'euler", type=float)
parser.add_argument("-n", "--number", help="la puissance de n dans a = A+BV^{n}", type=float)
parser.add_argument("-s", "--scatter", help="show scatters", action="store_true")
args = parser.parse_args()

A = args.A 
B = args.B
dt = args.dt
n = args.number if args.number else 1

plt.figure()
plt.title(f"a = {A} - {B}"+f'{r"$V^{n}$"}' + "\n" + r"$V_{n} = V_{n-1} + \frac{d}{dt}(a_{n-1})*\Delta t$")

plt.ylabel("V (m/s)")
plt.xlabel("temps (s)")

def recurse(liste, A,B, speed, velocity, dt):
    liste.append(speed)
    if round(velocity, 3) == 0:
        new_speed = speed + velocity*dt
        liste.append(new_speed)
    else:
        new_speed = speed + velocity*dt
        new_velocity = A - B * (new_speed ** n)
        recurse(liste, A, B, new_speed, new_velocity, dt)    

y_axis = []
initial_speed = 0
recurse(y_axis, A, B, initial_speed, A, dt) # sans vitesse initiale
print(len(y_axis))
x_axis = [dt*i for i in range(len(y_axis))]
plt.plot(x_axis, y_axis, label="Vitesse")
if A:
    line_inter = np.linspace(0, y_axis[-1]/A, 100)
    plt.plot(line_inter, A * line_inter, 'C1--', linewidth=2)
plt.legend(loc="best")
if args.scatter:
    plt.scatter(x_axis, y_axis, linewidths=1, color='red', s=15)
plt.show()
