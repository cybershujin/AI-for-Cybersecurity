# Prepends an element "___" with a value of 0 to indicate that a word is not present
# Converts your current dictionary of words:frequency to a dictionary of word:frequency_index_when_sorted_in_descending_order

word_index = {k[0]:i+1 for i, k in enumerate(sorted(word_dictionary, key=lambda k_v: k_v[1], reverse=True))}
word_index["___"] = 0

#this particulary word choice is because in this example I'm using it to look at email bodies
for word in ("the", "a", "from", "recipient", "email", "monday", "kindly", "congratulations"):
    print(f'{word}\t{word_index[word]}')

#output should look like:
# the	1
# a	5
# from	21
# recipient	1798
# email	43
# kindly	45
# monday	388
# congratulations	3011
