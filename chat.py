import random  # Importing random module for generating random responses
import json  # Importing json module for handling JSON data

import torch  # Importing PyTorch for neural network operations

from model import NeuralNet  # Importing the neural network model class
from nltk_utils import bag_of_words, tokenize  # Importing utility functions for NLP

# Setting the device for PyTorch (GPU if available, otherwise CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Loading intents data from a JSON file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Loading the trained model data
FILE = "data.pth"
data = torch.load(FILE)

# Extracting model parameters and data for prediction
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initializing the neural network model and loading its state
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()  # Setting the model to evaluation mode

# Defining the bot's name
bot_name = "Regie"


def get_response(msg):
    # Tokenizing the input message
    sentence = tokenize(msg)

    # Converting the tokenized sentence into a bag-of-words vector
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])  # Reshaping for model input
    X = torch.from_numpy(X).to(device)  # Converting to a PyTorch tensor

    # Getting the model's output prediction
    output = model(X)
    _, predicted = torch.max(output, dim=1)  # Getting the index of the highest predicted score

    # Mapping the predicted index to a tag
    tag = tags[predicted.item()]

    # Calculating the probabilities of each class
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # If the highest probability is above a threshold, return a response
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                # Returning a random response from the matched intent
                return random.choice(intent['responses'])

    # Default response if no intent is confidently matched
    return "I don't understand. My knowledge only covers the 2021-2022 NBA season. Can you specify the year you're referring to so I can assist you better?"