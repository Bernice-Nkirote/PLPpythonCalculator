def addition(x,y):
    return x + y

def subtraction(x,y):
    return x-y

def multiplication(x, y):
    return x * y

def division(x,y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        x / y


print("Select operation:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")


while True:
    choice = input("Enter choice (1/2/3/4):")

    if choice in ("1,2,3,4"):
        num1 = float(input("Input first number: "))
        num2 = float(input("Input second number: "))

        if choice == "1":
            print("Result:", addition(num1, num2))
        elif choice == "2":
            print("Result:", subtraction(num1, num2))
        elif choice == "3":
            print("Result:", multiplication(num1,num2))
        elif choice == "4":
            print("Result:", division(num1,num2))
        break
    else:
        print("invalid input")



        
