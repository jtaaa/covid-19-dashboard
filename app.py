# -*- coding: utf-8 -*-
import dash
import os

from Home import Home


# ---
# App setup
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# ---


# ---
# Set layout
app.layout = Home()
# ---
