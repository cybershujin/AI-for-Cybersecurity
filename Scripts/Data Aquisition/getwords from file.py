def get_words(file_name):
    # We'll use a regular expression to find things that are not words or spaces.
    regex = re.compile("[^\w\s]")
    # Start with an empty list
    words = list()
    # Open the specified file
    with open(file_name, encoding='utf8', errors='ignore') as f:
        # Grab all of the lines
        text = f.readlines()
        # Set a flag to keep track of whether we have reached the body or not.
        finished_header = False
        # Iterate over the lines
        for line in text:
            # The last line in the headers is consistently the subject line.  If
            # we have not yet seen the subject then we are still parsing headers
            # and should ignore them.
            if finished_header:
                # If we have seen subject line, let's strip out things that aren't words
                # spaces, lowercase the line, and split it on whitespace.  Each word in
                # this list is then appended to the accumulating word list.
                for word in re.sub(regex, '', line.lower()).split():
                    words.append(word)
            # Check to see if the beginning of the line contains "subject:"
            # to determine if we have reached the end of the email header.
            elif line.lower() == "\n":
                # If we have, set the flag
                finished_header = True
    return words

get_words('../file/path/to/filename')
