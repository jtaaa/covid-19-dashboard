CONFIRMED_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
RECOVERED_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
DEATHS_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


datasources = {
    "confirmed_ts": {
        "url": CONFIRMED_URL,
        "name": "Confirmed cases timeseries data",
        "filename": "confirmed_ts.csv",
    },
    "recovered_ts": {
        "url": RECOVERED_URL,
        "name": "Recovered timeseries data",
        "filename": "recovered_ts.csv",
    },
    "deaths_ts": {
        "url": DEATHS_URL,
        "name": "Deaths timeseries data",
        "filename": "deaths_ts.csv",
    },
}
