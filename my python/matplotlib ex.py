from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
overs=np.arange(1,21)
scores=[9,2,4,7,8,13,6,7,3,5,3,3,12,13,33,26,36,22,34,25]
plt.bar(overs,scores,color="maroon")
plt.title("Sunrisers Over Wise Score")
plt.xlabel("Overs From 1 to 20")
plt.ylabel("Runs Based On Overs")
plt.xticks(overs)
plt.grid(axis='y',linestyle='-',color='black')
plt.show()
