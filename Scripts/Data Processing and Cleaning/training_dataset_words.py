# Use your get_file_list() function to obtain a list of all of the files and paths in the ../data/Enron/ham/ path
# Use your get_words() function to read in the words from each message
# Use your tokenize_email() function to convert each email into a list of word numbers using 1000 words
# Assemble all of these into a numpy array named x_ham_data
# Determine the shape of the resulting numpy array

WordsToWorkWith = 5000
list_data = list()
for file in get_file_list("../data/Enron/ham"):
    list_data.append(tokenize_email(get_words(file), words=WordsToWorkWith))
    
x_ham_data = np.array(list_data, dtype=object)
x_ham_data.shape
