import json
def data_loader(path_to):
    with open(path_to) as json_file:
        data = json.load(json_file)
        
        print(type(data))
    return data


if __name__ == "__main__":
    _data = data_loader(r'C:\fastapi_streetart_map\data\streetart.json')
    print(_data.keys())
    for k,v in _data.items():
        for _item in v:
            pass
            #print(_item)
            
