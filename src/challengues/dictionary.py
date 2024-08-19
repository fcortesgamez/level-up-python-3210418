import pickle


def save_dict(dict, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(dict, f)


def load_dict(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)
