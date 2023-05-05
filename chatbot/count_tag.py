import json

with open('intents.json') as file:
    data = json.load(file)

tag_count = len(data['intents'])

print(f'There are {tag_count} tags in the intents.json file.')
