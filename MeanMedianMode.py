#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# crea un data set ficticio centrado alrededor de los 27000
# con distribucion normal y desviacion estandar de 15000 con 10000 data points
incomes =  np.random.normal(27000, 15000, 10000)
print "Mean: ",np.mean(incomes)
print "Median: ",np.median(incomes)


# Moda: creamos un data set de 500 edades entre los 19 y 99 years
ages = np.random.randint(18, 99, 500)
print "Mode: ", stats.mode(ages)

plt.hist(incomes, 50)
plt.show()
