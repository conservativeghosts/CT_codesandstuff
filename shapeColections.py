import random

def shapeColector():
    colection1 = []
    colection2 = []
    colection3 = []


    print ("We're gonna be colecting shapes because why not")

    while True:
        Shapes = ["triangle/s", "cirle/s", "square/s", "rectangle/s"]
        Color = ["blue", "orange", "yellow", "green", "red", "brown"]

#colection one stuff
        for x in range(0,1):
            num1 = [random.randint(1, 100)]
            colection1.append (num1)
            color1 = Color[random.randint (0, 5)]
            colection1.append (color1)
            shape1 = Shapes[random.randint(0, 3)]
            colection1.append (shape1)

        for x in range (0,1):
            num2 = [random.randint(1, 100)]
            colection2.append (num2)
            color2 = Color[random.randint (0,5)]
            colection2.append (color2)
            shape2 = Shapes[random.randint(0,3)]
            colection2.append (shape2)
        
        for x in range (0,1):
            num3 = [random.randint(1, 100)]
            colection3.append (num3)
            color3 = Color[random.randint (0,5)]
            colection3.append (color2)
            shape3 = Shapes[random.randint(0, 3)]
            colection3.append (shape3)
       
        print("Your First colection of shapes is {}".format (colection1))
        print("Your second colection of shapes is {}".format (colection2))
        print("Your third colection of shapes is {}".format (colection3))

        newColect = input("Would you like to recreate your colections? Y/N: ")
        print("Thank you")
        if newColect.lower() == "n":
            break

        colection1.clear()
        colection2.clear()
        colection3.clear()

        print("Your new colections:")
if __name__=="__main__":
    shapeColector()
