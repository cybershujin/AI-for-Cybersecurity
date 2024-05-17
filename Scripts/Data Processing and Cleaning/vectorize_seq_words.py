# Implement a function named vectorize_sequence that accepts numpy array of shape (n,) where each row represents a list of word index numbers
# Your function must also accept a dimension value
# Your function should multi-hot encode the input list of word indices representing emails. Use the dimension value to define the number of features in your multi-hot encoded array
# Return the multi-hot encoded array
#note that this example is using the spam / legit email analysis example
#if you have not imported numpy yet uncomment this next line
#import numpy as np
  
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

## afer this, you'll to vectorize this so you have labels
x_legit_vectorized = vectorize_sequence(x_legit_data)
x_spam_vectorized = vectorize_sequence(x_spam_data)

#Merge the vectorized ham and spam into a single array. Add a column to this new array that contains a 0 to indicate legit and a 1 to indicate spam.

merged_data = np.append(x_legit_vectorized, x_spam_vectorized, axis=0)
labels = np.zeros(x_legit_vectorized.shape[0])
labels = np.append(labels, np.ones(x_spam_vectorized.shape[0]))
labels = labels.reshape(labels.shape[0],1)
all_data = np.append(labels, merged_data, axis=1)
all_data.shape
