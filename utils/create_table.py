# import psycopg2
# from config import config


_path = '..\data\STREET_ART.sql'

def load_file(_path):
    with open(_path, encoding = 'utf-8') as file: # Use file to refer to the file object
        data = file.read()
    return data


def create_tables(_input):

    commands = ''

if __name__ == "__main__":
    print(load_file(_path))
