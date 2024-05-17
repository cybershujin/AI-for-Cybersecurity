# Part 2, a reverse word index dictionary after you created the dictionary using the aquisition scripts and then reverse sorted it into a dictionary 

reverse_word_index = {k:v for v, k in word_index.items()}

def tokenize_email(text, words=100):
    """
    Accepts a list of words and a number of words from the dictionary to use.  Returns
    a list of word indices for each word.
    """
    word_array = [word_index[w] if word_index[w] < words else 0 for w in text]
    return word_array

def untokenize_email(indices):
    """
    Accepts a list of word indices.  Returns a list of words.
    """
    return [reverse_word_index[i] for i in indices]
    
print(' '.join(untokenize_email(tokenize_email(get_words('../data/file/path/filename'), words=10000))))

# arbitrarily I am limiting this to 10k words, but you can do whatever you like. this is just trying to optomize for processing time
