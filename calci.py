def add(number1, number2):
    print( number1 + number2)
def sub(number1, number2):
    print(number1 - number2)
def mult(number1,number2):
    print( number1 * number2 )
def Div(number1, number2):
     print( number1 / number2)
def Enter():
    print("Enter   your operation")
    operation=input()
    if (operation == "Addition" ):
        add(number1, number2)
        Enter()
    elif(operation == "Subraction" ):
        sub(number1, number2)
        Enter()
    elif(operation == "Multiplication" ):
        mult(number1,number2)
        Enter()
    elif(operation == "Division"  ):
        Div(number1, number2)
        Enter()
    elif(operation=="QUIT" ):
        print()
    else:
        print(" YOU HAVE ENTERED THE WRONG SUITABLE OPERATION")
        print("Enter any  suitable operation which is given below")
        print('Like')
        print("Addition")
        print("Subraction")
        print("Multiplication")
        print("Division")
        Enter()
# number1 = float(input("enter the number")) or int(input("enter the number"))
# number2 = float(input("enter the humber")) or int(input("enter the  number"))
try:
     number1 = float(input("enter the number")) or int(input("enter the number"))
     number2 = float(input("enter the humber")) or int(input("enter the  number"))
     print("Enter any suitable operation which is given below")
     print("Like  Addition   Subraction       Multiplication       Division")
     Enter()
except:
    print("Enter any Decimal or Integer")





