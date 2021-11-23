# visualizaiton_folium

IMPORTANT:
To run the Dash maps, you will need to install Dash. run the following code in terminal: pip install dash==1.16.3

Visit this website for more information: https://dash.plotly.com/installation

--------------------------------------------------------------------------------------------------------

View the path of several cars depicted with their aggressions in a Traffic Control Center dashboard.

# Contents:

**dashMapAsh3_6.py:** full dashboard-- 

  --Left:
  
    -- box with information on selected car
    
    -- line graph that plots aggression of last 16 seconds (before intersection) of car's path
    
    -- bar graph that shows the real time changing of lanes and aggressions of selected car's path of last 16 seconds (before intersection) (does NOT autoplay)
    
  --Right:
  
    -- main map graph: cars are represented by colored dots and are clickable. color corresponds with legend on right side
    
    
    
**3DforDash.py:** matplotlib 3D bar graph that shows the intersection aggression 10 seconds up to the intersection (not completed)

  -- x: seconds until intersection
  
  -- y: aggression categories (0-10, 10-20, etc until 100)
  
  -- z: percentage of total cars that have that aggression at that time til intersection
  
  -- should be incorporated into dashMapAsh3_6 eventually
  


**3DIntersection.csv:** a file you will need in order to run 3DforDash.py

  
**trigAdjust.ipynb:** function that adjusts the position of a car into the center of its lane no matter what lane number you provide it


**MultiLineVisualization.ipynb:** shows the animated plotting of any number of cars in real time

  -- limitation: cars are not clickable, so had to move to javascript + Dash
  

  
**CurrentPointVisualization.ipynb:** same thing but for one car only


_ALL OTHER CSV FILES_ are simply data files for different cars

_ALL "USE"_ files are for the sole purpose of the USEdashboard.html file to work.

Remember that you MUST change the file paths within each program to match the file path on your own device before runnning.

_ALL OTHER FILES_ are simple dependencies, css pages, and other files that help the code run.

# OLD: 

**dashboardMockUp.html:** better idea of dashboard with real visualization at the top and 4 graphs at bottom

**tabs.html:** better dashboard; tabs for different directions, clickable cars, and a popup historical map

**path.html:** rough idea of dashboard... top 2/3s is map, bottom left contains information of car selected, bottom right is intersection information (graph to come)

--------------------------------------------------------------------------------------------------------

If you have any questions, feel free to reach out to ashnakhetan@gmail.com!
