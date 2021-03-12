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
            print("Choose one of the following options Type a number ONLY!")
            choice = input("""1. Add to list,
2. Return a value at an index position
3. randomly search an item from your list
4. end program
    """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif  choice == "3":
                randoSearch()
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
        
        
def indexValues():
    try:
        indexPos = input("What index position would you like to pull a number from?   ")
        print(mylist[int(indexPos)])
    except:
        print("I'm sorry you need to start counting with the number 0")

def randoSearch():
    print("Here's a random walue from you list")
    print(listyBoi[random.randint(0, len(listyBoi)-1)])
    
if __name__== "__main__":
    mainProgram()
