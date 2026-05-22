import datetime

LOG_FILE = "data/votes.log"

def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} : {message}\n")