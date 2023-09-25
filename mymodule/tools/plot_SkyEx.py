import matplotlib.pyplot as plt
import numpy as np

ID,RA,Dec = np.loadtxt('/home/venturae/Desktop/PhD/ADACS_workshop/Monday/mymodule/data/output/catalog.csv', unpack = True, delimiter=',')

plt.scatter(RA, Dec)
plt.xlabel('RA [deg]')
plt.ylabel('Dec [deg]')
plt.show()
