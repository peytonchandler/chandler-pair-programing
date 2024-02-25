import numpy as np

def normalize(array):
    """Parameters
    _______
    c : ndarrary 
    
    Inputs_________
    An array
    
    Returns________
    Normalized array in range [0.0, 1.0]
        """
    assert(type(array)==np.ndarray)
    Amin = np.min(array)
    Amax = np.max(array)
    return (array - Amin)/(Amax - Amin)
    