import string
def wordCount():

    #Inputs a word to look for
    look = input("Enter a word: ")
    #n for counting
    n = 0
    
    #Change path here
    path = "/Users/John Biton/College Code/CSE S23/CSE 106/Lab 1/"
    with open(path + 'PythonSummary.txt', 'r') as file:

        #a = file.read()
        #a.lower()
        look.lower()
        

        for line in file:
            for word in line.split():
                word_lower = word.lower()
                for ele in word_lower: 
                    if ele in string.punctuation:
                        word_lower = word_lower.replace(ele, '')

                if(look == word_lower or look in word_lower):
                    n += 1

    print ("The word " + look + " occurs " + str(n) + " times ")

    file.close()

wordCount()