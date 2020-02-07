import json

def print_keys(data):
    for key, value in data.items():
        print("Key:")
        print(key)

with open('ccc.json', 'rt') as f:
    ccc = json.load(f)

print(ccc['toc_nodes']['toc-1']['text'])
print_keys(ccc['page_nodes']['toc-1'])

