# Implement a function named vectorize_sequence that accepts numpy array of shape (n,) where each row represents a list of word index numbers
# Your function must also accept a dimension value
# Your function should multi-hot encode the input list of word indices representing emails. Use the dimension value to define the number of features in your multi-hot encoded array
# Return the multi-hot encoded array
#note that this example is using the spam / legit email analysis example
  
def vectorize_sequence(word_index_array, dimension=WordsToWorkWith):
    """
    Accepts a numpy array of ragged rows.  Converts to a multihot encoded numpy array
    of length len(word_index_array) and `dimension` attributes in each row
    """
    results = np.zeros((len(word_index_array), dimension))
    for i, word in enumerate(word_index_array):
        results[i, word] = 1.0
    return results

vectorize_sequence(x_spam_data).shape
