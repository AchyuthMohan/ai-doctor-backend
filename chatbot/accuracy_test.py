import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import confusion_matrix

from model import NeuralNet
from nltk_utils import bag_of_words,tokenize
# Load the intents data
with open('intents.json') as f:
    intents = json.load(f)

# Load the trained model
data = torch.load("data.pth")
input_size = data['input_size']
output_size = data['output_size']
hidden_size = data['hidden_size']
all_words = data['all_words']
tags = data['tags']

model_state = data['model_state']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

# Prepare the testing data
X_test = []
y_test = []

for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        bag = bag_of_words(w, all_words)
        X_test.append(bag)
        label = tags.index(tag)
        y_test.append(label)

X_test = np.array(X_test)
y_test = np.array(y_test)

# Convert testing data to PyTorch tensors
X_test = torch.from_numpy(X_test).to(device)
y_test = torch.from_numpy(y_test).to(device)

# Set the model to evaluation mode
model.eval()

# Get the predicted labels for the testing data
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, dim=1)

# Calculate the confusion matrix
cm = confusion_matrix(y_test.cpu(), predicted.cpu())
print("Confusion Matrix:")
print(cm)

# Calculate the accuracy
accuracy = np.trace(cm) / np.sum(cm)
print("Accuracy:", accuracy)
