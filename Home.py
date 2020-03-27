import dash_core_components as dcc
import dash_html_components as html

from components.Timeseries.Layout import TimeseriesLayout
from textwrap import dedent as d


def Home():
    layout = html.Div(children=[
        dcc.Markdown(d("""
            # Hello! Welcome to my Covid-19 dashboard thingy.

            All data is downloaded from [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data).
        """)),
        TimeseriesLayout,
    ])
    return layout
