# this gets the words and then sorts them into a dictionary where it is sorted by frequency and paired with a number that represents the number of times that word appears in the file
# more efficent way of doing this is at https://github.com/cybershujin/AI-for-Cybersecurity/blob/main/Scripts/Data%20Processing%20and%20Cleaning/dict_frequency.py
all_words = dict()
for file in get_file_list("../data/file/path/filename"):
    words = get_words(file)
    for word in words:

        if all_words.__contains__(word)==True:
            all_words[word] = all_words[word]+1
        else:
            all_words[word] = 1
            
print(len(all_words))
word_dictionary = sorted(all_words.items(), key=lambda key_value: key_value[1], reverse=True)
word_dictionary[:5]
