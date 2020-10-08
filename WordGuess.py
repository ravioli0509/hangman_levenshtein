import random
from SecretWord import SecretWord

class WordGuess:

    def __init__(self, wordDic):
        #attributes 
        self.secretWord = SecretWord()
        self.wordDic = wordDic
        self.num_guess = 0 #set the number of guess to 0
        self.hint = "" 
        self.guesses = [] #store the user guesses in a list
    def play(self):
        """ Plays out a single full game of Word Guess """
        self.chooseSecretWord() 
        s1 = str(self.secretWord) #s1 is a jumbled word
        s2 = str(self.secretWord.sort()) #s2 is sorted
        Edit = self.editDistance(s1,s2) #Uses the editDistance and assigns Edit to a numerical value
        self.num_guess = self.calculatingGuess(Edit)  #using the function calculating guess function,
        # and Edit as the argument. self.num_guess becomes this edit value 
        while self.num_guess > 0 and not self.secretWord.isSolved():            
            guess = self.getGuess() #user guess
            if guess == "*": 
                print("Hint: " + self.hint)
                self.num_guess -= 1 #decrements after user asks for hint
                continue
            if self.secretWord.update(guess): #progress
                pass
            else:
                self.num_guess -= 1 #decrements if the update is not true, which means user got the wrong letter
            self.guesses.append(guess) #avoids user to input the same letter again        
        if self.secretWord.isSolved(): #to check if user got the whole word
            print("You Solved the Puzzle!")
            print("The secret word was :"+str(self.secretWord)) #Congratulate
        else: 
            print("You Failed!")
            print("The secret word was :"+str(self.secretWord)) #Say condolences 
        return

    def calculatingGuess(self, editDistance):
        editDistance *= 2 
        if editDistance < 5: 
            return 5 #edit distance will be 5 no matter how low it can go
        if editDistance > 15:
            return 15 #edit distance will be 15 no matter how high it can go
        return editDistance

    def chooseSecretWord(self):
        """ Chooses the secret word that will be guessed """
        key = random.choice(list(self.wordDic)) #randomly chooses the word from the self.wordDic
        self.secretWord.setWord(key) 
        self.hint = self.wordDic[key] #the key for every secret word will be the hint
        print("A secret word has been randomly chosen!")
        return 

    def editDistance(self, s1, s2):
        #In this function, levenshtein distance is used
        # The function is credited by https://www.python-course.eu/
        if s1 == "": #(Base cases)
            return len(s1) #returns the len of s1 if its a string
        if s2 == "":    
            return len(s2) #returns the len of s2 if its a string
        if s1[-1] == s2[-1]: # checks if the last letter of the words are the same in s1 and s2
            cost = 0 #the cost of moving the letter will be 0 if s1 and s2 are the same
        else:
            cost = 1 #cost becomes 0
        #minCost will be finding the minimum of 3 editDistance functions 
        minCost = min([self.editDistance(s1[:-1], s2)+1, #adds 1 cost using s1[:-1] and s2
                self.editDistance(s1, s2[:-1])+1, #adds 1 cost using s1 and s2[:-1]
                self.editDistance(s1[:-1], s2[:-1]) + cost]) #adds cost using s1[:-1] and s2[:-1]
        return minCost
        #returns minCost, which is the minimum numbers of cost there is to find out the distance

    def getGuess(self):
        """ Queries the user to guess a character in the secret word """
        print("You have "+str(self.num_guess)+" guesses remaining")
        print("Word Guess Progress ", end = "")
        self.secretWord.printProgress() #prints the _ with letters, if the user guessed some
        prompt = input("Enter a character that has not been guessed or * for a hint: ")
        while prompt in self.guesses: #Avoids repetition of the same  letter
            print("Invalid Guess. You have already guessed this letter")
            prompt = input("Enter a character that has not been guessed or * for a hint: ")
        return prompt
        #TODO