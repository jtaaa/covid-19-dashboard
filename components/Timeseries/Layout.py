import dash_core_components as dcc
import dash_html_components as html
import re

from textwrap import dedent as d
from components.Timeseries.Utils import regions, DEFAULT_SELECTED_REGIONS, getOptions


TimeseriesLayout = html.Div(children=[
    dcc.Markdown("## Confirmed Cases by Region"),
    html.Div(children=[
        html.Div(children=dcc.Graph(id="confirmed-cases"),
                 className="four columns"),
        html.Div(children=dcc.Graph(id="recoveries"),
                 className="four columns"),
        html.Div(children=dcc.Graph(id="deaths"),
                 className="four columns")
    ], className="row"),
    dcc.Markdown(d("""
        # Region Selector

        Please select the regions you want to see on the graph above of total confirmed cases from 24th of January to present.
    """)),
    dcc.Input(id="region-search", type="text",
              placeholder="Country or region"),
    dcc.Checklist(
        id="region-selector",
        options=getOptions(),
        value=DEFAULT_SELECTED_REGIONS
    ),
])
