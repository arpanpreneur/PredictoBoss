import matplotlib.pyplot as plt
import numpy as np
import Datasets as DS

df = DS.getDataSet_petrol("16-06-2018")


plt.plot(df['date'],df['price'].astype('float'))

plt.show()

