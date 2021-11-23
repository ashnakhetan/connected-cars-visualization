# importing libraries
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import random

# load the file
data_file_path = '/Users/ashnakhetan/Desktop/Ashna/ConnectedCars/IntersectionData.csv'
df = pd.read_csv(data_file_path)

# flatArray is an array of all the aggression values without the seconds, etc
array = np.array(df.iloc[:, 1:4])
flatArray = array.flatten()
random.shuffle(flatArray)

# set the graph style
style.use('ggplot')

# define the figure and its type (3D)
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# empty arrays for values to come
x = []
y = []
dz = []

# the number of bars will be the number of seconds (11) times the number of cars
numCars = len(df. columns)-1
# because one column is the seconds column
numBars = 11*numCars

# x_pos is where each bar starts on the x-axis. This should be ex. [10,10,10,9,9,...] for a graph of 3 cars
x_pos = [10] * numCars + [9] * numCars + [8] * numCars + [7] * numCars + [6] * numCars + \
    [5] * numCars + [4] * numCars + [3] * numCars + \
    [2] * numCars + [1] * numCars + [0] * numCars
# y_pos is same for y-axis. Should be ex [1,2,3,1,2,3,...] for 3 cars
y_pos = []
for x in range(1, numCars+1):
    y_pos.append(x)
y_pos *= 11
# z will always begin at 0 (floor)
z_pos = np.zeros(numBars)

# each increment on the x and y axes is by 1
x_size = np.ones(numBars)
y_size = np.ones(numBars)
z_size = flatArray

# create 3D bar graph and assign color
ax1.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='orange')

# set axes of graph
plt.xlim(10, 0)
plt.ylim(1, 3)
ax1.set_zlim(0, 100)

# set labels
ax1.set_xlabel('Time to Intersection')
ax1.set_ylabel('% of Vehicles in Level')
ax1.set_zlabel('Aggression Level')

# display the graph!
plt.show()
