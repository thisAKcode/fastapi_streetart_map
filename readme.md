### fastapi for serving geospatial data

# Stack: Fastapi, JQuery & Leaflet

I use FastAPI to serve data from a database. 
Data loaded into db from json. Each of these objects contains lat, lon,


The project consists of two parts: a backend stack including server/fastapi app and tools for visualizing data.

## Backend

The web server serves db data via api endponints that allows user to return data that can be consumed 
by fronend. 
In future live web site real data can be made available.

## Frontend

Tool to handle spatial data in json format and render it on leaflet canvas.


## Running
```
uvicorn app:main --reload
```

## Requirements
All modules are available through pypi for python tools and via cdn for js tools/frameworks. 



## other stuff

https://fastapi.tiangolo.com/advanced/templates/
https://pybit.es/articles/how-to-handle-environment-variables-in-python/


Access postges db with Python Fastapi backend and Leaflet.js. Use HTMX to minimize javascript complexity.

Concept is visually presented here:

![part1](./part1.jpg)
![part2](./part2.jpg)

