import torch  # Importing PyTorch
import torch.nn as nn  # Importing PyTorch's neural network module


class NeuralNet(nn.Module):
    # Defining the neural network architecture
    def __init__(self, input_size, hidden_size, num_classes):
        # Initialize the class by calling the parent class's constructor
        super(NeuralNet, self).__init__()

        # Defining the first linear layer with specified input and hidden sizes
        self.l1 = nn.Linear(input_size, hidden_size)

        # Defining the second linear layer with the hidden size as both input and output
        self.l2 = nn.Linear(hidden_size, hidden_size)

        # Defining the third linear layer with the hidden size as input and the number of classes as output
        self.l3 = nn.Linear(hidden_size, num_classes)

        # Applying ReLU activation function
        self.relu = nn.ReLU()

    def forward(self, x):
        # Forward pass through the first layer and applying ReLU activation
        out = self.l1(x)
        out = self.relu(out)

        # Forward pass through the second layer and applying ReLU activation
        out = self.l2(out)
        out = self.relu(out)

        # Forward pass through the third layer (output layer)
        out = self.l3(out)

        # No activation function and no softmax at the output layer, as this will be handled during loss calculation
        return out