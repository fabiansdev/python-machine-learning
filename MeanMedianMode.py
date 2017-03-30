#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# crea un data set ficticio centrado alrededor de los 27000
# con distribucion normal y desviacion estandar de 15000 con 10000 data points
incomes =  np.random.normal(27000, 15000, 10000)
print np.mean(incomes)

plt.hist(incomes, 50)
plt.show()

