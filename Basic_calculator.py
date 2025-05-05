def calculator():
    number1 = float(input("Enter first number :"))
    operation = input ("Enter the operation you would like to perform (+,-,*,/):")
    number2 = float( input("Enter first number :"))

    if operation == '+':
        return number1+number2
    elif operation == '-':
        return number1-number2
    elif operation == '*':
        return number1*number2
    elif operation == '/':
        return number1/number2
    else:
        return "Invalid operation"

print(calculator())
