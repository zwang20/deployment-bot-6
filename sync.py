"""
sync.py

syncs the database
"""

import os
import subprocess
import time

os.chdir("db-database")
while True:
    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", "database-update"])
    subprocess.call(["git", "push", "--force"])
    subprocess.call(["git", "pull"])
    time.sleep(60)
