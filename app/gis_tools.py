import json
# from shapely import wkb, wkt
from geojson import Feature, Point

_relgeom = ['lat', 'lon', 'geom']

def data_loader(path_to):
    with open(path_to) as json_file:
        data = json.load(json_file)        
    return data

def make_feature(geom, proper):
    my_point = Point([float(geom.get('lon'  or "")), 
                      float(geom.get('lat'  or ""))
                      ]
                    )
    return Feature(geometry=my_point, properties=proper)

def to_geojson(_data):
    _features = []

    for k,v in _data.items():

        for _item in v:
            _geom1 = {}
            _props1 = {}
            _keys = (list(_item.keys()))
            for i in _keys:
                if i in _relgeom:
                    _geom1[i] = _item[i]
                else:
                    _props1[i] = _item[i]
            _item = make_feature(_geom1, _props1)
            _features.append(_item)
    return _features


if __name__ == "__main__":
    _data = data_loader(r'C:\fastapi_streetart_map\data\streetart.json')
    geo_j = to_geojson(_data)
    geo_j2 = (json.dumps(geo_j[0]))
    
#_wkt_geom = wkt.loads('POINT(-2.5378432182396935 55.20394960316738)')
#_wkb_geom = wkb.dumps(g, hex=True, srid=4326) 
