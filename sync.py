"""
sync.py

syncs the database
"""

import os
import subprocess
import time
import datetime
import logging

while True:
    logging.info("\t%s Pushing to database", datetime.datetime.now())
    env = dict(os.environ)
    env["TZ"] = "UTC"
    subprocess.call(["date", ">", "data.txt"], env=env)
    os.chdir("db-database")
    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", "database-update"])
    subprocess.call(["git", "push", "--force"])
    os.chdir("..")
    logging.info("\t%s Pulling from database", datetime.datetime.now())
    os.chdir("db-database")
    subprocess.call(["git", "pull"])
    os.chdir("..")
    time.sleep(60)
