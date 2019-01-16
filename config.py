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
    "imgquality":80,
    "defaultzoom":5,
    "minzoom":4,
    "maxzoom":6,
    "texturepath": "/root/.minecraft/versions/1.13.2/1.13.2.jar"
    }

renders["mini"] = {
    "world": os.environ['SERVER_NAME'],
    "title": "Small",
    "dimension": "overworld",
    "rendermode": "normal",
    'crop': (-512, -512, 512, 512),
    "minzoom":4,
    "maxzoon":4,
    "imgformat": "png",
    "texturepath": "/root/.minecraft/versions/1.13.2/1.13.2.jar"
}


outputdir = "/var/www/html"
