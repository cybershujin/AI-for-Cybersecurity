# Use your get_file_list() function to obtain a list of all of the files and paths in the ../data/Enron/ham/ path
# Use your get_words() function to read in the words from each message
# Use your tokenize_email() function to convert each email into a list of word numbers using 1000 words
# Assemble all of these into a numpy array named x_ham_data
# Determine the shape of the resulting numpy array

WordsToWorkWith = 5000
list_data = list()
for file in get_file_list("../data/filepath/filename1"):
    list_data.append(tokenize_email(get_words(file), words=WordsToWorkWith))
    
x_ham_data = np.array(list_data, dtype=object)
x_ham_data.shape

#notice the filename1 and filename2 below
# you will need to do this as many times as you have classifications
# so if your labels on the data are "legit" and "spam" for emails
# you need to do this for legitemails and spamemails 
#legitemails filename1 and spamemails filename2 for example

list_data = list()
for file in get_file_list("../data/filepath/filename2"):
    list_data.append(tokenize_email(get_words(file), words=WordsToWorkWith))
    
x_spam_data = np.array(list_data, dtype=object)
x_spam_data.shape

## after this, you'll need to do the vectorize_sequence
