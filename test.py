import json

def print_keys(data):
    #prints all of the keys in a dictionary
    for key, value in data.items():
        print("Key:")
        print(key)

with open('ccc.json', 'rt') as f:
    ccc = json.load(f)

s = ''

print_keys(ccc['page_nodes'])

#find all of the text blocks from the CCC
for i in range(1, 396):
    try:
        string = 'toc-' + str(i)
        for item in ccc['page_nodes'][string]['paragraphs']:
            for item2 in item['elements']:
                if item2['type'] == 'text':
                    #if the item is a block of text, add it to the string
                    s += item2['text'] + '\n'
    except:
        pass

#Save them all to a file
with open('ccc.txt', 'w') as f: 
    f.write(s)
