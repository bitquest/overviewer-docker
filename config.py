# Importing the os python module
import os
worlds[os.environ['SERVER_NAME']] = "/world/"

renders["normalrender"] = {
    "world": os.environ['SERVER_NAME'],
    "title": "World",
    "dimension": "overworld",
    "rendermode": "normal",
    'crop': (-500, -500, 500, 500),
    "imgformat": "jpg",
    "defaultzoom":6,
    "minzoom":4
}

outputdir = "/var/www/html"