# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import re
# import argparse
import pandas as pd
import numpy as np
from textwrap import dedent as d
from dash.dependencies import Input, Output
from datamanager import importData, datasources


# ---
# Argumemnt parsing
# parser = argparse.ArgumentParser()
# parser.add_argument("-f", "--fresh",
#                     action='store_true',
#                     help="Import fresh data from github repo (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data).")
# args = parser.parse_args()
# ---

# ---
# Data loading
confirmed = pd.read_csv("confirmed_ts.csv")
confirmed = confirmed.groupby("Country/Region").sum().reset_index()

confirmed_x = confirmed.columns[range(5, len(confirmed.columns))]


def getData(includedRegions):
    return list(map(
        lambda series: {
            'x': confirmed_x,
            'y': series[range(5, len(series))],
            'name': series[0]
        },
        confirmed.loc[
            confirmed["Country/Region"].map(lambda x: x in includedRegions),
        ].to_numpy(),
    ))


regions = confirmed["Country/Region"]


def getOptions(query=""):
    return list(map(lambda x: {
        'label': x, 'value': x
    }, filter(lambda x: re.search(query, x, re.IGNORECASE), regions)))
# ---


# ---
# App setup
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
server.secret_key = os.environ.get('secret_key', os.urandom(24))

app.layout = html.Div(children=[
    dcc.Markdown(d("""
        # Hello! Welcome to my Covid-19 dashboard thingy.

        All data is downloaded from [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data).
    """)),
    dcc.Graph(
        id="confirmed-cases",
        figure={
            'data': getData([]),
            'layout': {
                'title': 'Confirmed Cases'
            }
        }
    ),
    dcc.Markdown(d("""
        # Region Selector

        Please select the regions you want to see on the graph above of total confirmed cases from 24th of January to present.
    """)),
    dcc.Input(id="region-search", type="text",
              placeholder="Country or region"),
    dcc.Checklist(
        id="region-selector",
        options=getOptions(),
        value=[]
    ),
])
# ---

# ---
# Update callbacks


@app.callback(
    Output(component_id='confirmed-cases', component_property='figure'),
    [Input(component_id='region-selector', component_property='value')]


)
def update_selected_regions(includedRegions):
    return {
        'data': getData(includedRegions),
        'layout': {
            'title': 'Confirmed Cases'
        }
    }


@app.callback(
    Output(component_id='region-selector', component_property='options'),
    [Input(component_id='region-search', component_property='value')]
)
def update_selectable_regions(query):
    return getOptions(query if query else "")
# ---


# ---
# Main (entry)
if __name__ == '__main__':
    # if args.fresh:
    #     importData()
    app.run_server(debug=True)
# ---
