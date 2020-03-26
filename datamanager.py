import urllib.request
import pandas as pd
from utils.urls import CONFIRMED_URL

datasources = {
    "confirmed_ts": {
        "url": CONFIRMED_URL,
        "name": "Confirmed cases timeseries data",
        "filename": "confirmed_ts.csv",
    },
}


def importData():
    print("Data download beginning!")
    for key in datasources:
        datasource = datasources[key]
        filename, _ = urllib.request.urlretrieve(
            datasource["url"], filename=datasource["filename"])
        print("'{}' download complete".format(datasource["name"]))
        print("Download file location: ", filename)
    print("Data download complete!")


# ---
# Data loading
confirmed = pd.read_csv("confirmed_ts.csv")
confirmed = confirmed.groupby("Country/Region").sum().reset_index()

dates = confirmed.columns[range(5, len(confirmed.columns))]
# ---
