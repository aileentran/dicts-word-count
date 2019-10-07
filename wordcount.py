#thoughts! 
#takes in a file --> turning into list of words 
#split on white space 
#returning "key item" pair 

#open the file 
#split file into list of words 
#make empty dictionary 

#loop through the words 
#use dict.get to initialize/add to value count 

#print or return stuff 
def count_words(filename):
    poem = open(filename)
    # splits file into lines, it is now a list of each line
    lines = [line.rstrip().split() for line in poem]

    #removes newline character/whitespace from end of line
    # lines = [line.rstrip() for line in lines]
    # #splits each line into list of individual words
    # lines = [item.split(" ") for item in lines]
    # #list of ALL individual words!
    words = []
    for item in lines:
        words.extend(item)

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    for word in word_count:
        print(word, word_count[word])

    return word_count
    


count_words("twain.txt")

