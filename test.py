print("hi")
print("This is a calculator app please hold on")
total = 0
num1 = int(input("Please give me the first value : "))
num2 = int(input("Please give me the second value : "))
print("1 : +, 2 : -, 3 : *, 4 : /")
symbol = input("What calculation do you want to do ? () :")
print(Calculator(symbol))
def Calculator(symbol):
    if(symbol == "+"):
        total = num1 + num2
    elif(symbol == "-"):
        total == num1 - num2
    elif(symbol == "*"):
        total == num1 * num2
    elif(symbol == "/"):
        total == num1 / num2
    

