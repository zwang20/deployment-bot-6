#! /bin/bash

cd db-database
while true; do
    echo "Pushing to database"
    sudo chmod 777 -R .
    TZ='UTC'
    date > date.txt
    git add -A
    git commit -m "Database Sync from $(hostname)"
    git push --force
    echo "Pulling from database"
    git stash
    git fetch origin
    git reset --hard origin/main
    git pull
    git stash pop
    sleep 60
done
