"""
sync.py

syncs the database
"""

import os
import subprocess
import time
import datetime
import logging

os.chdir("db-database")
while True:
    logging.info("\t%s Pushing to database", datetime.datetime.now())
    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", "database-update"])
    subprocess.call(["git", "push", "--force"])
    logging.info("\t%s Pulling from database", datetime.datetime.now())
    subprocess.call(["git", "pull"])
    time.sleep(60)
