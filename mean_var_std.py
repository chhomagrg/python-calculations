import numpy as np

def calculate(input_list):
    # Validate input
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 Numpy array
    array = np.array(input_list).reshape(3, 3)

    # Perform calculations
    calculations = {
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean()],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum()]
    }

    return calculations