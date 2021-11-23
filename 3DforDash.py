# import libraries
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import mpld3
import base64
from io import BytesIO
import random
import matplotlib.colors as colors
import matplotlib.cm as cm
import math

# insert file path for your CSV
data_file_path = '/Users/ashnakhetan/Desktop/Ashna/ConnectedCars/IntersectionData.csv'
df = pd.read_csv(data_file_path)
df = df.iloc[:, :4]

# select and flatten the array so it only contains the 3 columns of aggression data
array = np.array(df.iloc[:, 1:4])
flatArray = array.flatten()

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

numCars = len(df. columns)-1
numBars = 11*numCars

# there will be an x value for each car at each second (10-0), thus making the total numCars*11
# UNLESS 2+ cars have the same aggression at the same second, then it gets confusing
x = [10] * numCars + [9] * numCars + [8] * numCars + [7] * numCars + [6] * numCars + \
    [5] * numCars + [4] * numCars + [3] * numCars + \
    [2] * numCars + [1] * numCars + [0] * numCars
# this is me filling the aggressions with random values to test it out
y = [70] * numCars + [20] * numCars + [80] * numCars + [50] * numCars + [60] * numCars + \
    [50] * numCars + [30] * numCars + [60] * numCars + \
    [10] * numCars + [20] * numCars + [0] * numCars
# for j in range(0, 30):
#     n = random.randint(0, 100)
#     y.append(n)
# z will always start at 0s because you want them all to start on the floor
z = np.zeros(numBars)

# the change in x and y will always be 1 (square base for bars)
dx = np.ones(numBars)
dy = np.ones(numBars)

multArr = np.ones(numCars)
# dzz will be our array that stores the % of cars that contain the specified aggression at each level
dzz = []

# using our flatArray from before to create dzz
for i in range(0, numCars):
    flatArray[i] = flatArray[i]/10
    flatArray[i] = math.floor(flatArray[i])
    flatArray[i] = flatArray[i]*10
    print(flatArray[i])
    for j in range(0, numCars):
        if (i != j):
            if (flatArray[i] == flatArray[j]):
                multArr[i] += 1
    dzz.append((multArr[i]/numCars) * 100)

dzz *= 11
print(dzz)

# fake dz to test it out beforehand; can delete
dz = [100] * numCars + [90] * numCars + [80] * numCars + [70] * numCars + [60] * numCars + \
    [50] * numCars + [40] * numCars + [30] * numCars + \
    [20] * numCars + [10] * numCars + [0] * numCars

# must figure out a way to change color based on y, not on x or z
cols = ['red', 'blue', 'yellow', 'green']

# I don't think this does much
offset = dzz + np.abs(min(dzz))
fracs = offset.astype(float)/offset.max()
norm = colors.Normalize(fracs.min(), fracs.max())
colors = cm.jet(norm(fracs))

# create plot!
ax1.bar3d(x, y, z, dx, 10, dzz, color=colors)

# set axis limits
plt.xlim(10, 0)
# plt.ylim(1, 3)
ax1.set_zlim(0, 100)

# set labels
ax1.set_xlabel('Time to Intersection')
ax1.set_ylabel('Aggression Level')
ax1.set_zlabel('% of Vehicles in Level')

# plot!
plt.show()
