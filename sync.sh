#! /bin/bash

while true; do
    echo "Pushing to database"
    sudo chmod 777 -R .
    export TZ="UTC"
    date > data.txt
    cd db-database
    git add -A
    export TZ="UTC"
    git commit -m "$(date) $(hostname)"
    git push
    echo "Pulling from database"
    git stash
    git fetch origin
    git reset --hard origin/main
    git pull --rebase
    git stash pop
    cd ..
    sleep 60
done
