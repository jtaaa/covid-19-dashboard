import re

from data.manager import confirmed, dates


DEFAULT_SELECTED_REGIONS = ['Trinidad and Tobago', 'Canada']
regions = confirmed["Country/Region"]


def getData(includedRegions):
    return list(map(
        lambda series: {
            'x': dates,
            'y': series[range(5, len(series))],
            'name': series[0]
        },
        confirmed.loc[
            confirmed["Country/Region"].map(lambda x: x in includedRegions),
        ].to_numpy(),
    ))


def getOptions(query=""):
    return list(map(lambda x: {
        'label': x, 'value': x
    }, filter(lambda x: re.search(query, x, re.IGNORECASE), regions)))
