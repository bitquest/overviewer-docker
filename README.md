# overviewer-docker
A Docker image with Minecraft Overviewer to create a map of a Minecraft world

## requirements
1. docker
2. docker-compose

## how to build
```
docker-compose build
```

## how to run
Included, there is a test docker-compose.yml file that will search for a 'world' folder in the same path as the yml file and serve it as a overviewer map. If you plan to use this in a production server you might want to create another docker-compose.yml file from scratch with the location of your minecraft world.

The example docker-compose.yml included in this repo will spawn a server in http://localhost:5000

To create (or update the map) you must run
```
docker exec -it overviewer ./overviewer.py --config=config.py
```