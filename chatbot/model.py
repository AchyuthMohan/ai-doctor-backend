import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        # initialization to different layers of input is done here
        super(NeuralNet, self).__init__()
        # here performs the linear transformation
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
# there are three layers first second and final layers
# first and second arebasically the inputs ie the input message after linear transformation will be passed through l1 and l1

# the output will be returned to final layer
# relu is an activation function which turns on when non negative input is there or else it turns to zero

#  forward function is actually used to generate the output and pass the same to final layer.
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)  # rectified linear unit
        out = self.l3(out)
        # no activation and no softmax
        return out
# This architecture can be used for various classification tasks, where the number of classes is specified by num_classes.
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# model = NeuralNet(input_size,hidden_size,output_size).to(device)
