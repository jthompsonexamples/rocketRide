# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:27:15 2022

@author: bexar
"""

# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
from itertools import chain

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(
    children=[
        html.H1(
            'SpaceX Launch Records Dashboard',
            style={
                'textAlign': 'center',
                'color': '#503D36',
                'font-size': 40
                }
            ),
        # TASK 1: Add a dropdown list to enable Launch Site selection
        # The default select value is for ALL sites
        # dcc.Dropdown(id='site-dropdown',...)
        html.Br(),
        html.Div(
            dcc.Dropdown(
                id = 'launch-site',
                options = 
                    # [{'label': i, 'value': i} for i in spacex_df['Launch Site'].unique()],
                    [{'label': i, 'value': i} for i in list(chain.from_iterable([pd.array(['All']), spacex_df['Launch Site'].unique()]))],
                placeholder = 'Select Launch Site',
                style = {
                    'width':'80%',
                    'padding':'3px',
                    'font-size':'20px',
                    'text-align-last':'center'
                    }
                )
            ),
        # TASK 2: Add a pie chart to show the total successful launches count for all sites
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        html.Div(
            dcc.Graph(
                id='success-pie-chart'
                )
            ),
        html.Br(),

        html.P(
            "Payload range (Kg):"
            ),
        # TASK 3: Add a slider to select payload range
        #dcc.RangeSlider(id='payload-slider',...)
        html.Div(
            dcc.RangeSlider(
                id='payload-range',
                min = 0,
                max = 10000,
                #step = 500,
                marks = {i: str(i) for i in range(0,10001,500)},
                value = [0, 10000]
                )
            ),
        # TASK 4: Add a scatter chart to show the correlation between payload and launch success
        html.Div(
            dcc.Graph(
                id='success-payload-scatter-chart'
                )
            ),
        ]
    )

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# callback decorator
@app.callback([Output(component_id = 'success-pie-chart', component_property = 'figure'),
               Output(component_id = 'success-payload-scatter-chart', component_property = 'figure')],
              [Input(component_id = 'launch-site', component_property = 'value'),
               Input(component_id = 'payload-range', component_property = 'value')])

def analysisFunc(launchSite, payloadRange):
    if(launchSite == 'All'):
        pieOut=px.pie(spacex_df[['class','Mission Outcome']].groupby('class').count(),
                 values = 'Mission Outcome',
                 names = ['Failure','Success'],
                 title = 'Success Rate')
    else:
        pieOut=px.pie(spacex_df.loc[spacex_df['Launch Site'] == launchSite,['class','Mission Outcome']].groupby('class').count(),
             values = 'Mission Outcome',
             names = ['Failure','Success'],
             title = 'Success Rate')
    scatOut = px.scatter(spacex_df.loc[(spacex_df['Payload Mass (kg)'] >= payloadRange[0]) & (spacex_df['Payload Mass (kg)'] <= payloadRange[1]),:],
               x = 'Payload Mass (kg)',
               y = 'class',
               color = 'Booster Version Category')
    return([pieOut, scatOut])
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()