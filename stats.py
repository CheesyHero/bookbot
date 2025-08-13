

def get_num_words():
    with open("/Users/guestuser/webflyx/bookbot/books/frankenstein.txt") as f:
    # do something with f (the file) here 
    # f is a file object
        file_contents = f.read()

    file_split = len(file_contents.split(None));
    resultString = str(file_split) + " words found in the document";

    return resultString;
    
def get_char_used():
    with open("/Users/guestuser/webflyx/bookbot/books/frankenstein.txt") as f:
    # do something with f (the file) here 
    # f is a file object
        file_contents = f.read()

    file_contents = file_contents.lower();
    file_dictionary = {};

    for s in file_contents:
        
        if s in file_dictionary:
            file_dictionary[s] += 1
        
        else:
            file_dictionary[s] = 1

    return file_dictionary;