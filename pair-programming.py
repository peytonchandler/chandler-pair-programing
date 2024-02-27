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
 
### Feedback ###
#This overall looks good, however there are a few things you could add
#The data type(s) for your inputs and outputs are never explicilty listed, so that would be a good thing to add
#Your assert message could also be expanded upon, for example you could say "Incorrect type for array, please input a np.ndarray"
#I like how you setup your function, it is very clean and easy to interpret
    
def normalize_test():
    """
    ___________________________________________
    General Info
    This function serves only as a test for the normalize function created by Peyton Chandler
    This function requires the numpy module
    ___________________________________________
    Inputs
    None
    ___________________________________________
    Returns
    Nothing
    ___________________________________________
    Prints
    If both tests are sucessful, a message indicating that the function has passed all tests will be printed
    An error message will be printed if any of the tests are failed
    ___________________________________________
    Tests
    Test 1: Determines whether the normalize function works for a range of integers from 0 to 10
    Test 2: Determines whether the normalize function works with values of vastly different magnitudes  
    ___________________________________________
    """
    test_1_array = np.arange(0,11,1)
    assert np.min(normalize(test_1_array)) == 0 and np.max(normalize(test_1_array)) == 1, 'Normalize function failed test 1. Function does not work for a range of integers from 0 to 10'
    test_2_array = np.array([1e-6,1e6,1e-10,1e10])
    assert np.min(normalize(test_2_array)) == 0 and np.max(normalize(test_2_array)) == 1, 'Normalize function failed test 1. Function does not work with inputs of vastly different magnitudes'
    print('All tests passed')