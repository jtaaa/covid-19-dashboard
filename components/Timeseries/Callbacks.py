import re

from app import app
from dash.dependencies import Input, Output
from components.Timeseries.Utils import confirmed, dates, getData, getOptions


@app.callback(
    [Output(component_id="confirmed-cases", component_property="figure"),
     Output(component_id="recoveries", component_property="figure"),
     Output(component_id="deaths", component_property="figure")],
    [Input(component_id="region-selector", component_property="value")]
)
def update_selected_regions(includedRegions):
    return [{
        'data': data,
        'layout': {
            'title': title
        }
    } for data, title in zip(getData(includedRegions), ['Confirmed Cases', 'Recoveries', 'Deaths'])]


@app.callback(
    Output(component_id="region-selector", component_property="options"),
    [Input(component_id="region-search", component_property="value")]
)
def update_selectable_regions(query):
    return getOptions(query if query else "")
