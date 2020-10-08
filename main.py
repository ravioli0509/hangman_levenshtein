from WordGuess import WordGuess


def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    File = open(filename) 
    Dict = {} #open dictionary
    for line in File:
        temp = line.split(' ') #splits the line with space
        Dict[temp[0]] = temp[1] #setting a dictionary for every line
    File.close()
    return Dict

def main():
    prompt = input("Please eneter a Word Guess input file: ") #asks the user to input file name
    readFile = readWords(prompt) 
    wordGuess = WordGuess(readFile)
    wordGuess.play() #plays the game 
    while input("Would you like to play again (Y/N) ?").upper() == "Y": 
        wordGuess = None #if user wants to play again, we reset the game, by setting wordGuess to none 
        wordGuess = WordGuess(readFile) 
        wordGuess.play() # and let it play again
    

    

if __name__ == "__main__":
    main()