import matplotlib.pyplot as plt
import numpy as np

study = [1,2,3,4,5,6,7]
score = [50,58,65,72,80,88,95]

m, b = np.polyfit(study,score,1)

predict = m*8 + b

print("Predicted score is:",predict)
plt.scatter(study,score)

x = np.array([1,8])

y = m*x + b

plt.plot(x,y)
plt.show()