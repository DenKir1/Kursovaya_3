import json
path = '../operations.json'
def read_file(path):
    '''
    :param path: str path to json file
    :return: dict from file
    '''
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data

