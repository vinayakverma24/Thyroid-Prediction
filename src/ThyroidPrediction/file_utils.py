import pickle
import os 

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def save_model(model, model_filename):
    with open(model_filename, 'wb') as model_file:
        pickle.dump(model, model_file)

def save_encoder(encoder, encoder_filename):
    with open(encoder_filename, 'wb') as encoder_file:
        pickle.dump(encoder, encoder_file)
