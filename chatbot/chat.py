import random
import json
import os
import torch
from chatbot.model import NeuralNet
from chatbot.nltk_utils import bag_of_words,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open(os.path.join(os.getcwd(), 'intents.json'), 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE, map_location=torch.device('cpu'))


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]



model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name ="Dr. Matrix"
print("Dr. Matrix - your virtual Doctor. With quick responses, our AI bot is here to provide you with medical support ands assitance, anytime and anywhere.")
print("Let's chat! (type 'quit' to exit)")
def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence,all_words)
    # print("all_words",all_words)
    # print("X: ",X)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    if prob.item()>0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                # print(tag)
                
                # print(random.choice(intent['responses']))
                return random.choice(intent['responses'])

    return "Sorry ! I cant recognize the symptoms . Try again"
    # else:
        # print(f"{bot_name}: I am Sorry But couldn't get recognize the symptoms.")
        


# torch module is used to search for all words from intents file 
# after getting all words we create a binary list of 0 and 1 to note the pressence of a word in the given message
# 