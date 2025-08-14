

def get_num_words(location):
    with open(location) as f:
    # do something with f (the file) here 
    # f is a file object
        file_contents = f.read()

    file_split = file_contents.split(None) 

    return len(file_split)
    
def get_char_used(location):
    with open(location) as f:
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

def print_sorted_dictionaries(my_dict):

    sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1])) 

    for key, value in my_dict.items(): 
        k = str(key);
        v = str(value);
        s = k + ": " + v
        print(s)

        