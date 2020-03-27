import re

from app import app
from dash.dependencies import Input, Output
from components.Timeseries.Utils import confirmed, dates, getData, getOptions


@app.callback(
    Output(component_id="confirmed-cases", component_property="figure"),
    [Input(component_id="region-selector", component_property="value")]
)
def update_selected_regions(includedRegions):
    return {
        'data': getData(includedRegions),
        'layout': {
            'title': 'Confirmed Cases'
        }
    }


@app.callback(
    Output(component_id="region-selector", component_property="options"),
    [Input(component_id="region-search", component_property="value")]
)
def update_selectable_regions(query):
    return getOptions(query if query else "")
