import numpy as np

def normalize(array):
    """
    ___________________________________________
    Parameters
    c : ndarrary 
    ___________________________________________
    Inputs
    An array that will be normalized
    ___________________________________________
    Returns
    Normalized array in range [0.0, 1.0]
    ___________________________________________
    """
    assert(type(array)==np.ndarray), 'Incorrect type for array'
    Amin = np.min(array)
    Amax = np.max(array)
    return (array - Amin)/(Amax - Amin)
    