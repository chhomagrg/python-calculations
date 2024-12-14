import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(input_list).reshape(3, 3)

    return {
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), float(array.mean())],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), float(array.var())],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), float(array.std())],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), int(array.max())],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), int(array.min())],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), int(array.sum())]
    }
