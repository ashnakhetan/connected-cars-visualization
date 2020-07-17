# connected-cars-visualization
Plotting and animating the path of cars utilizing their aggressiveness scores and other traffic information.

In this repository, I will include my Python code for plotting and animating the math of any number of cars on a road/map snapshot. I have also uploaded the resulting html files. 

Features:
- Lines showing the historical path of each car
- OR The single-point path of a car WITHOUT historical depiction
- Lines are colored to depict the aggressiveness of the car (yellow is low and red is high, as per the legend at the top)
- A timestamp slider is featured at the bottom to view the car's path at any moment in time
- You may include an unlimited number of cars by altering just the implicit parameter of the functions
- SOON: will include html code as a "dashboard", through which one can view an intersection's aggressiveness snapshot and specific details of a single selected car

MultiLineVisualization.ipynb : The Python code for the path of a car SHOWING history as well.
Multi1.html : The resulting html animation.

CurrentPointVisualization.ipynb : The Python code for the path of a car WITHOUT history.
Current1.html : The resulting html animation.
