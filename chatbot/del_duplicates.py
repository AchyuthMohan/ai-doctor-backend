import json

with open('intents.json') as file:
    data = json.load(file)

tags = [intent['tag'] for intent in data['intents']]
duplicates = {tag: tags.count(tag) for tag in set(tags) if tags.count(tag) > 1}

if not duplicates:
    print('No duplicate tags found.')
else:
    print(f'{len(duplicates)} duplicate tags found.')
    for tag, count in duplicates.items():
        print(f'Deleting {count-1} instances of tag "{tag}".')
        for intent in data['intents']:
            if intent['tag'] == tag:
                data['intents'].remove(intent)
                count -= 1
                if count == 1:
                    break

with open('intents.json', 'w') as file:
    json.dump(data, file, indent=4)
