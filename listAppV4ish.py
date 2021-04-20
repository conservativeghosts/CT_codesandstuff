import random 
"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from a specific intex positions
"""
listyBoi = []
unique = []

def mainProgram():
    while True:
        try:
            print("yo, we're gonna work with some lists now")
            print("Choose one of the following options Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of stuff to list
3. Return a value at an index position
4. Sort your list
5. randomly search an item from your list
6. search for a specific item /(linear search/)
7. recursive binary search
8. iterative binary search
9. print lists
10. end program
    """)
            if choice == "1":
                addToList()
            elif  choice == "2":
                addMuchStuff()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(listyBoi)
            elif choice == "5":
                randoSearch()
            elif choice == "6":
                linSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique, 0, len(unique)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique, int(binSearch))
                if result != -1:
                    print ("your number is at index postition {}".format(result))
                else:
                    print("your number cannot be found in that list...")
            elif choice == "9":
                printLists()
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

def sortList(listyBoi):
    for x in listyBoi:
        if x not in unique:
            unique.append(x)
    unique.sort()
    show = input("you wanna see your new list?   Y/N")
    if show.lower() == "y":
        print(unique)
        
def indexValues():
    try:
        indexPos = input("What index position would you like to pull a number from?   ")
        print(mylist[int(indexPos)])
    except:
        print("I'm sorry you need to start counting with the number 0")

def randoSearch():
    print("Here's a random walue from you list")
    print(listyBoi[random.randint(0, len(listyBoi)-1)])

def linSearch():
    print("this is bad people don/'t realy do this, but let us search bad")
    searchThing = input("What number are you looking to find")
    for x in range (len(listyBoi)):
        if listyBoi[x] == int(searchThing):
            print("your idem is at index position {}".format(x))

def recursiveBinarySearch(unique, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique[mid] == x:
            print("wow, what luck your number is at index postition {}".format(mid))
            return mid
        
        elif unique[mid] > x:
            return recursiveBinarySearch(unique, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique, mid+1, high, x)
    else:
        print("your number isn't here")

def iterativeBinarySearch(unique, x):
    low = 0
    high = len(unique)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique[mid] < x:
            low = mid + 1
        elif unique[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def printLists():
    if len(unique) == 0:
        print(listyBoi)
    else:
        which1 = input("Which list would you like to print?   Sorted or Un-sorted")
        if which1.lower() == "sorted":
            print(listyBoi)
        elif which1.lower() == "un-sorted":
            print(unique)
        

if __name__== "__main__":
    mainProgram()
