import json

def print_keys(data):
    for key, value in data.items():
        print("Key:")
        print(key)

with open('ccc.json', 'rt') as f:
    ccc = json.load(f)

s = ''

print_keys(ccc['page_nodes'])

for i in range(1, 396):
    try:
        string = 'toc-' + str(i)
        for item in ccc['page_nodes'][string]['paragraphs']:
            for item2 in item['elements']:
                if item2['type'] == 'text':
                    s += item2['text'] + '\n'
    except:
        "hi"

with open('ccc.txt', 'w') as f: 
    f.write(s)