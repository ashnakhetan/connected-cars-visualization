# import libraries needed
import dash  # (version 1.0.0)
import random
import dash_table
import pandas as pd
import numpy as np
import dash_core_components as dcc
import plotly.express as px

import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.offline as py  # (version 4.4)
import plotly.graph_objs as go

import matplotlib
import matplotlib.pyplot as plt

from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import mpld3
import base64
from io import BytesIO

from itertools import chain

import plotly.graph_objects as go
from plotly.validators.scatter.marker import SymbolValidator

# initialize variables to be used for the interval setting
r = 0
nEnd = 98
nStart = nEnd-16
car_files = []

# this is the one place where user has to update file names to fetch the different car files
car_files = ['visualization_1_time', 'visualization_2_time',
             'visualization_3_time', 'visualization_4_time', 'visualization_5_time', '2291-3']
numCars = len(car_files)
# a dictionary that contains the file addresses of each car
car_dict = {}
for i in range(1, numCars):
    car_dict[str(i)] = pd.read_csv(str(
        "/Users/ashnakhetan/Desktop/Ashna/Dash/Dash_Map/" + str(car_files[i]) + '.csv'))

# initialize the arrays for our graph axes
agg = []
ro = []
y = []

# access token to get a base map layer from Mapbox; may have to get your own
mapbox_access_token = "pk.eyJ1IjoiYXNobmFrMDMiLCJhIjoiY2s5OTdiYW1wMXBhbDNlcGcwY2plcjhuMyJ9.gMhq8HNZMti-CWHXP3-lTA"

# defining colorscales
colorscales = px.colors.named_colorscales()

# this function takes your aggression and aggression range and turns it into a color
# for that aggression
# I don't think we currently use this


def getColor(agg, agg_range):
    yellowGvalue = 1
    redGvalue = .2
    aggPercentage = 1-(agg-agg_range[0])/(agg_range[1]-agg_range[0])
    greenValue = (yellowGvalue-redGvalue)*aggPercentage+redGvalue
    # we define the color based on the greenValue,
    # red and blue values are 255 and 51, it will scale to yellow as
    # the green value changes
    return matplotlib.colors.to_hex([1, greenValue, .2])


app = dash.Dash(__name__)

blackbold = {'color': 'black', 'font-weight': 'bold'}

# set up layout of entire page
app.layout = html.Div([
    # ---------------------------------------------------------------
    html.Div([
        html.Div([
            # box at top of page
            html.Label(['Selected Car Details:'], style=blackbold),
            html.Pre(id='web_link', children=[],
                     style={'white-space': 'pre-wrap', 'word-break': 'break-all',
                            'border': '1px solid black', 'text-align': 'center',
                            'padding': '12px 12px 12px 12px', 'color': 'blue',
                            'margin-top': '3px'}
                     ),
            # graph at middle left
            html.Div(dcc.Graph(id='lineGraph', children=[], config={'displayModeBar': False, 'scrollZoom': True},
                               style={'background': '#00FC87', 'padding-bottom': '.5px',
                                      'padding-left': '2px', 'padding-right': '2px', 'height': '35vh'}
                               )),
            # graph at bottom left
            html.Div(id='graphDiv', children=[dcc.Graph(id='aggGraph', config={
                     'displayModeBar': False})], style={'display': 'none'}),
            # animation_options={'auto_play':True}

            # intersection 3D graph that doesn't work right now
            # html.Div(dcc.Graph(id='intersectionGraph', children=[], config={'displayModeBar': False, 'scrollZoom': True},
            #                    style={'background': '#00FC87', 'padding-bottom': '.5px',
            #                           'padding-left': '2px', 'padding-right': '2px', 'height': '35vh'}
            #                    )),
            html.Div(id='none', children=[], style={'display': 'none'}),
        ], className='three columns'
        ),

        # main Map graph on right
        html.Div([
            dcc.Graph(id='graph', children=[], config={'displayModeBar': False, 'scrollZoom': True},
                      style={'background': '#00FC87', 'padding-bottom': '.5px',
                             'padding-left': '2px', 'padding-right': '2px', 'height': '97vh'}
                      ),
            # set the interval for its updates
            dcc.Interval(
                id='graph-update',
                interval=1*300,
                n_intervals=0,
                max_intervals=nEnd
            ),
        ], className='nine columns'
        ),
    ], className='row'
    ),
], className='twelve columns'
)

# callback function for main map graph
@app.callback(Output('graph', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph(n_intervals):
    # if time is less than end time, append the new coordinates and aggression
    if (n_intervals <= nEnd):
        lat = []
        for i in range(1, numCars):
            lat.append(car_dict[str(i)].loc[n_intervals, 'latitude'])

        lon = []
        for i in range(1, numCars):
            lon.append(car_dict[str(i)].loc[n_intervals, 'longitude'])

        colorA = []
        for i in range(1, numCars):
            colorA.append(
                getColor(car_dict[str(i)].loc[n_intervals, 'aggresiveness score'], [0, 100]))

        # notes:
        # use dictionary here too
        # assign a color to each aggressiveness score
        # just retrieve the color for the corresponding agg score instead of creating list
        # try not to expand array as time increases

        carDetail = []
        carDetail.append(1)
        carDetail.append(2)
        carDetail.append(3)
        carDetail.append(4)
        carDetail.append(5)

        # more notes:
        # use this (change to dictionary) to store the info (history points)
        # store a 2D sequence of the history points (appending)

        # create the graph now
    locations = [
        go.Scattermapbox(
            lat=lat,
            lon=lon,

            marker=go.scattermapbox.Marker(
                size=5,
                # symbol='square',f
                # color=getColor(agS[n_intervals], aggRange) <-- don't use this function anymore
                color=colorA,
                showscale=True,
                colorscale=[[0, 'yellow'], [1, 'red']],
                cmin=0,
                cmax=1,
                colorbar=dict(
                    tickmode='array',
                    tickvals=[],
                    thickness=15,
                )
            ),
            unselected={'marker': {'opacity': 1}},
            # selected={'marker': {'opacity': 0.5, 'size': 25}},
            # hoverinfo='text',
            # hovertext=colorA,
            # customdata=df_sub['website']
            customdata=carDetail,
        ),
    ]
    # return figure
    return {
        'data': locations,
        'layout': go.Layout(
            height=670,
            width=980,
            margin={'t': 0, 'l': 0, 'b': 0, 'r': 0},
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,
                style='satellite-streets',
                center=dict(
                    lat=42.3051448,
                    lon=-83.6926055
                ),
                pitch=40,
                zoom=17,

            ),
        )
    }
# ---------------------------------------------------------------

# callback for the middle left graph (we call it Line Graph)


@app.callback(
    Output('lineGraph', 'figure'),
    [Input('graph', 'clickData'),
     Input('graph-update', 'n_intervals')]
)
def update_graph(clickData, n_intervals):
    if clickData is None:
        return {}
    # when you click a car, this will activate
    else:
        if n_intervals < nStart:
            return {}
        else:
            carNum = clickData['points'][0]['customdata']
            print(carNum)
            # appends the aggression values for the selected car for the last 16 seconds
            for i in range(carNum, carNum+1):
                agg.append(
                    round(car_dict[str(i)].loc[n_intervals, 'aggresiveness score'], 2))
                y.append(0)
                ro.append(nEnd-(car_dict[str(i)].loc[n_intervals, 'row']))

                # must fix this to actually display the car id like the weblink does
                carId = 'carId'

            fig2 = px.scatter(
                # mode='lines+markers',
                # marker=dict(size=10, symbol=41),
                x=ro,
                y=agg,
                # symbol=41,
                color=agg,
                range_x=[16, 0],
                range_y=[0, 100],
                # for us, yellow to red is 0 to 100 in aggression
                color_continuous_scale=px.colors.sequential.YlOrRd,
                title='Real Time: ' + carId,
                range_color=[0, 100],
                labels={
                    "x": "Seconds to intersection",
                },
            )
            fig2.update_yaxes(title=None, showticklabels=True)
            fig2.update_layout(
                margin=dict(l=30, r=0, t=20, b=40),
                paper_bgcolor="White",
                font=dict(
                    # family="Courier New, monospace",
                    size=8,
                    # color="RebeccaPurple"
                )
            )

            return fig2
# ---------------------------------------------------------------

# callback for the box in the upper left (we call it Web Link)


@app.callback(
    Output('web_link', 'children'),
    [Input('graph', 'clickData'),
     Input('graph-update', 'n_intervals')]
)
def display_click_data(clickData, n_intervals):
    if clickData is None:
        return 'Click on any bubble'
    # when car is clicked, information about the car will be displayed
    else:
        carNum = clickData['points'][0]['customdata']
        the_link = (str(car_files[carNum]) + ', Lane: ' + str(car_dict[str(carNum)].loc[n_intervals, 'lane']) + "\n" + ' Latitude: ' + str(car_dict[str(carNum)].loc[n_intervals, 'latitude']) + "\n"+'Longitude: ' +
                    str(car_dict[str(carNum)].loc[n_intervals, 'longitude']) + "\n" + 'Aggression Score: ' + str(round(car_dict[str(carNum)].loc[n_intervals, 'aggresiveness score'], 2)))

        if the_link is None:
            return 'No car selected'
        else:
            return html.A(the_link)
# ---------------------------------------------------------------

# callback for the graph in the bottom left (we call it Agg Graph)


@app.callback(
    Output('aggGraph', 'figure'),
    [Input('graph', 'clickData'),
     Input('graph-update', 'n_intervals')]
)
def display_aggGraph(clickData, n_intervals):
    if clickData is None:
        return {}
    # when car is clicked, it's lane and aggression information is displayed
    else:
        if n_intervals < nStart:
            return {}
        else:
            # set variables for use in graph
            carNum = clickData['points'][0]['customdata']
            car = car_dict[str(carNum)]['lane'][nStart:nEnd]
            aggression = car_dict[str(
                carNum)]['aggresiveness score'][nStart:nEnd]
            row = car_dict[str(carNum)]['row'][nStart:nEnd]

            print(carNum)

            # create the graph
            fig = px.bar(
                x=car,
                y=aggression,
                color=aggression,
                # range_color=[-10,48],              # differentiate color of marks
                opacity=0.9,
                orientation="v",              # 'v','h': orientation of the marks
                barmode='relative',
                text=round(aggression, 2),
                color_continuous_scale=px.colors.sequential.YlOrRd,
                range_color=[0, 100],
                animation_frame=row,
                range_x=[1, 5],
                range_y=[0, 100],
                title='Aggression in last 15 seconds',
                template='ggplot2',
                labels={
                    "x": "Lane",
                    "y": "Aggression"
                },
            )
            return fig

# this part displays the graphDiv if an element is clicked and the time is greater than or equal to start time


@app.callback(
    Output(component_id='graphDiv', component_property='style'),
    [Input('graph', 'clickData'),
        Input('graph-update', 'n_intervals')]
)
def show_element(clickData, n_intervals):
    if clickData is None:
        return {'display': 'none'}
    else:
        if n_intervals < nStart:
            return {'display': 'none'}
        else:
            return {'display': 'block'}
# ---------------------------------------------------------------

# intersection 3D graph that doesn't work right now (we call it 3D Graph)
# @app.callback(
#     Output('intersectionGraph', 'figure'),
#     [Input('graph', 'clickData'),
#      Input('graph-update', 'n_intervals')]
# )
# def display_intersectionGraph(clickData, n_intervals):
#     prevent_initial_call = True
#     if clickData is None:
#         return {}
#     else:
#         if n_intervals < nStart:
#             return {}
#         # elif n_intervals == nEnd:
#             # return {
#         else:
#             data_file_path = '/Users/ashnakhetan/Desktop/Ashna/ConnectedCars/IntersectionData.csv'
#             df = pd.read_csv(data_file_path)
#             # df = df[['Sec', 'Car1', 'Car2', 'Car3']]
#             df = df.iloc[:, :4]

#             array = np.array(df.iloc[:, 1:4])
#             flatArray = array.flatten()

#             style.use('ggplot')

#             fig = plt.figure()
#             ax1 = fig.add_subplot(111, projection='3d')

#             x = []
#             y = []
#             dz = []

#             cols = ['red', 'blue', 'yellow', 'green']
#             colours = []

#             numCars = len(df. columns)-1
#             numBars = 11*numCars

#             x_pos = [10] * numCars + [9] * numCars + [8] * numCars + [7] * numCars + [6] * numCars + \
#                 [5] * numCars + [4] * numCars + [3] * numCars + \
#                 [2] * numCars + [1] * numCars + [0] * numCars
#             z_pos = []
#             for x in range(1, numCars+1):
#                 z_pos.append(x)

#             z_pos *= 11
#             y_pos = np.ones(numBars)

#             x_size = np.ones(numBars)
#             z_size = np.ones(numBars)
#             y_size = flatArray

#             ax1.bar3d(x_pos, y_pos, z_pos, x_size,
#                       y_size, z_size, color='aqua')

#             plt.xlim(10, 0)
#             plt.ylim(0, 100)
#             ax1.set_zlim(1, 3)

#             ax1.set_xlabel('Time to Intersection')
#             ax1.set_zlabel('% of Vehicles in Level')
#             ax1.set_ylabel('Aggression Level')

#             return plt


# #--------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
