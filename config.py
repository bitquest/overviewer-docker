# Importing the os python module
import os
worlds[os.environ['SERVER_NAME']] = "/world/"
size=int(os.environ['SIZE'])

renders["overworld"] = {
    "world": os.environ['SERVER_NAME'],
    "title": "Big",
    "dimension": "overworld",
    "rendermode": "normal",
    'crop': (size*-1, size*-1, size, size),
    "imgformat": "jpg",
    "defaultzoom":6,
    "minzoom":2
}

renders["mini"] = {
    "world": os.environ['SERVER_NAME'],
    "title": "Small",
    "dimension": "overworld",
    "rendermode": "normal",
    'crop': (-1000, -1000, 1000, 1000),
    "imgformat": "png"
}


outputdir = "/var/www/html"