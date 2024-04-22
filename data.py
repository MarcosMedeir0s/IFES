import json

def load_data(filename):
    with open(filename, 'r') as arquivo:
        return json.load(arquivo)

def save_data(filename, data):
    with open(filename, 'w') as arquivo:
        json.dump(data, arquivo, indent=4)
