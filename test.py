import json

def print_keys(data):
    for key, value in data.items():
        print("Key:")
        print(key)

with open('ccc.json', 'rt') as f:
    ccc = json.load(f)

for item in ccc['page_nodes']['toc-2']['paragraphs']:
    for item2 in item['elements']:
        if item2['type'] == 'text':
            print(item2['text'])
        else:
            print(item2['type'])