from Node import Node

class LinkedList:
    """ The Singly-Linked List class defined in lecture """
    #in this Linked List class, setindex, findindex and getHead are added as new functions
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def findindex(self, index): #added function
        counter = 0  #we set the counter to 0 and current to the head of the list
        current = self.head
        while counter != index and current.getNext() != None :
            current = current.getNext() #traverses while current is not equal to index and the next current is not none
            counter += 1 
        return current.data #returns the data of the current node
    
    def setindex(self,index,data): #added function
        counter = 0 
        current = self.head
        while counter != index and current.getNext() != None:
            current = current.getNext()
            counter += 1 
        current.data = data #the whole function is same as the findIndex, its just setting current data to data

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1
    

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()

    def getHead(self): #added function
        return self.head #returns head of the linked list

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()

        # Additional attribute(s) go here:

    def setWord(self, word):
        """ Adds the characters in 'word' to self.linkedList in the given order """
        for char in word:
            self.linkedList.append(char) #appends every element in the word into the linked list
        
    def sort(self):
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        #Insertion sort
        secret = SecretWord()  
        secret.setWord(str(self)) #takes the words from the linkedlist to do an insertion sort
        for index in range(1,(secret.linkedList.length())): #iterates from 1 to the size of the linkedlist in the secret word
            currentvalue = secret.linkedList.findindex(index)
            position = index-1 #index decrements by 1 for the linkedlist
            while position >= 0 and secret.linkedList.findindex(position)>currentvalue: 
                # Move elements of secret.linkedList[0..i-1], that are 
                # greater than key, to one position ahead of their current position
                secret.linkedList.setindex(position+1, secret.linkedList.findindex(position))
                position = position-1
            secret.linkedList.setindex(position+1, currentvalue) 
            #the position will be +1 with the new current value after the while loop
        return secret

    def isSolved(self):
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        node = self.linkedList.getHead() #node becomes the head  
        while node != None:
            if node.display == True: #passes the if statement if the display is True
                pass
            else:
                return False #else returns False
            node = node.getNext() #traverses
        return True


    def update(self, guess):
        """ Updates the nodes in self.linkedList that match 'guess' """ 
        updated = False #start with setting updated as False
        node = self.linkedList.getHead() #node becomes the head
        while node != None:
            if node.data == guess: #if user's guess is same as data, we show the display and update it
                node.display = True
                updated = True
            node = node.getNext() #traverse
        return updated

    def printProgress(self):
        """ Prints the current game progress
        Ex: y _ l l _ w """
        node = self.linkedList.getHead() #node becomes the head
        while node != None:
            if node.display:
                print(node.data,end=" ") #if node display is true then it prints the data
            else:
                print("_",end = " ") #leaves the _ if the display is not true
            node = node.getNext()
        print()

    def __str__(self):
        """ Converts the characters in self.linkedList into a string """
        temp = ""
        node = self.linkedList.getHead() #node becomes the head
        while node != None:
            temp += node.data #adds the letter into empty string
            node = node.getNext() #traverse
        return temp


        