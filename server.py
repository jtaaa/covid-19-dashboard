import os
from app import app


# ---
# Import callbacks
import components.Timeseries.Callbacks
# ---


# ---
# Setup server
server = app.server
server.secret_key = os.environ.get('secret_key', os.urandom(24))
# ----


# ---
# Main (entry)
if __name__ == '__main__':
    app.run_server(debug=True)
# ---
