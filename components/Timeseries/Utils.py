import re

from data.manager import confirmed, recovered, deaths, dates


DEFAULT_SELECTED_REGIONS = ['Trinidad and Tobago', 'Canada']
regions = confirmed["Country/Region"]


def getSelectedData(df, includedRegions):
    return [
        {
            'x': dates,
            'y': series[range(5, len(series))],
            'name': series[0]
        }
        for series in
        df[df["Country/Region"].isin(includedRegions)].values
    ]


def getData(includedRegions):
    return [getSelectedData(df, includedRegions) for df in [confirmed, recovered, deaths]]


def getOptions(query=""):
    return list(map(lambda x: {
        'label': x, 'value': x
    }, filter(lambda x: re.search(query, x, re.IGNORECASE), regions)))
