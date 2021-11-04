#! /bin/bash

while true; do
    echo "Pushing to database"
    sudo chmod 777 -R .
    export TZ="UTC"
    date > data.txt
    cd db-database
    git add -A
    git commit -m "Database Sync from $(hostname)"
    git push --force
    echo "Pulling from database"
    git stash
    git fetch origin
    git reset --hard origin/main
    git pull
    git stash pop
    cd ..
    sleep 60
done
