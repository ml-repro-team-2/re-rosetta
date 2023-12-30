import pickle
import os

def save_array(array, filename):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)

    open_file = open(filename, "wb")
    pickle.dump(array, open_file)
    open_file.close()