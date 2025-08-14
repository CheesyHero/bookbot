
import sys
#fileLocation = "/Users/guestuser/webflyx/bookbot/books/frankenstein.txt";
if len(sys.argv) != 2:
    print("To use Bookbot: You must input the location of a .txt you wish to view.")

else:
    fileLocation = sys.argv[1]
    from stats import get_num_words;
    wordCount = get_num_words(fileLocation) 

    print("============ BOOKBOT ============" + "\n" +
      "Analyzing book found at " + fileLocation + "\n" +
      "----------- Word Count ----------" + "\n" + 
      "Found " + str(wordCount) + " total words" + "\n")

    from stats import get_char_used;
    from stats import print_sorted_dictionaries;
    print_sorted_dictionaries(get_char_used(fileLocation))

    print("============= END ===============")
