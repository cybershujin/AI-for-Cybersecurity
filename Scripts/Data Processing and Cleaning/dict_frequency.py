## this does the same thing as the other script just more efficently 
## this creates a diction of words that were found and then assigns the count of the times that word appears as its key with the value being the word
#then it orders the list by most to least frequent
# so if the word "llama" appears 23 times key llama in this dictionary will return a 23 as a vlaue
#then it prints the top 5 most common words
#output at the end looks like:
# 397577
# [('the', 245154), ('to', 192085), ('and', 140879), ('of', 122584), ('a', 121969)]


from collections import Counter

all_words = Counter()
for file in get_file_list("../data/file/path/filename"):
    words = get_words(file)
    all_words.update(words)
            
print(len(all_words))
word_dictionary = all_words.most_common(5)
print(word_dictionary)
