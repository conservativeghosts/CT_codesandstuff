import random 
"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from a specific intex positions
"""
listyBoi = []

def mainProgram():
    while True:
        try:
            print("yo, we're gonna work with some lists now")
            print("Apparently we're still working on this thing, so...")
            print("Choose one of the following options Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of stuff to list
3. Return a value at an index position
4. print list
5. randomly search an item from your list
6. search for a specific item
7. end program
    """)
            if choice == "1":
                addToList()
            elif  choice == "2":
                addMuchStuff()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                print(listyBoi)
            elif choice == "5":
                randoSearch()
            elif choice == "6":
                painSearch()
                #why, this is pain. Thanks god
            else:
                break
        except:
            print("An error occurred")

def addToList():
    try:
        whatAdd = input("What number would you like to add to your list   ")
        listyBoi.append(int(whatAdd))
        print(listyBoi)
    except:
        print("Bro, you need to type a number")

def addMuchStuff():
    print("let's add a bunch of numbers to our list")
    numAdd = input("how many items would you like to add?  ")
    numRange = input("What is the largest number possible that you want to be in your list?  ")
    for x in range (0, int(numAdd)):
        listyBoi.append(random.randint (0, int(numRange)))
    print("the list is compleate")
        
def indexValues():
    try:
        indexPos = input("What index position would you like to pull a number from?   ")
        print(mylist[int(indexPos)])
    except:
        print("I'm sorry you need to start counting with the number 0")

def randoSearch():
    print("Here's a random walue from you list")
    print(listyBoi[random.randint(0, len(listyBoi)-1)])

def painSearch():
    print("this is bad people don/'t realy do this/, but let us search bad")
    searchThing = input("What number are you looking to find")
    for x in range (len(listyBoi)):
        if listyBoi[x] == int(searchThing):
            print("your idem is at index position {}".format(x))
            
    
if __name__== "__main__":
    mainProgram()
