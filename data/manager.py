import pandas as pd
import data.cron


# ---
# Data loading
confirmed = pd.read_csv("confirmed_ts.csv")
confirmed = confirmed.groupby("Country/Region").sum().reset_index()

recovered = pd.read_csv("recovered_ts.csv")
recovered = recovered.groupby("Country/Region").sum().reset_index()

deaths = pd.read_csv("deaths_ts.csv")
deaths = deaths.groupby("Country/Region").sum().reset_index()

dates = confirmed.columns[range(5, len(confirmed.columns))]
# ---
