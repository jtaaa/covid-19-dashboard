import time
import atexit
import urllib.request
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from data.sources import datasources


scheduler = BackgroundScheduler()


# ---
# CRON job to download fresh data. Set to run every 4 hours.
@scheduler.scheduled_job(trigger="interval", hours=4, next_run_time=datetime.now(), id="download-confirmed")
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


scheduler.start()


# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
