# -*- coding: utf-8 -*-
import numpy as np
import math

a = 9.78 # Acceleration of the rocket in m/s^2
c = 299792458# Speed of light in m/s

dist = np.double(raw_input('\n\t How far is your star? (in light-years): '))
proper_time = 2.*((c/a)*math.asinh(((dist/2.)*365.25*24.*3600.)*a/c))/(365.25*24.*3600.)
print '\t It would take{0: 4.1f}'.format(proper_time)+' earth years approx. to get there at 1g.\n'

