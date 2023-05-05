import json

with open('intents.json') as file:
    data = json.load(file)

tags = [intent['tag'] for intent in data['intents']]
duplicates = {tag: tags.count(tag) for tag in set(tags) if tags.count(tag) > 1}

if not duplicates:
    print('No duplicate tags found.')
else:
    print('Duplicate tags found:')
    for tag, count in duplicates.items():
        print(f'{tag}: {count} duplicates.')
