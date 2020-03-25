import urllib.request

datasources = {
    "confirmed_ts": {
        "url": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
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
