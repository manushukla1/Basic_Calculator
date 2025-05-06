def calculator():
    while True:
        print("\nSimple Calculator")
        number1 = float(input("Enter first number: "))
        assert number1 >= 0, "Only Positive Number!"

        operation = input("Enter the operation you would like to perform (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            print("Goodbye!")
            break

        number2 = float(input("Enter second number: "))
        assert number2 >= 0, "Only Positive Number!"

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            assert number2 != 0, "Can't divide by zero"
            result = number1 / number2
        else:
            print("Invalid operation!")
            continue  # skip to next loop iteration

        print("Result:", result)
calculator()
# earlier in my code there were issues related to how i was calling the function --
"""
def calculator():
    while True:
        print ("\nSimple Calculator")
        number1 = float(input("Enter first number :"))
        assert number1 >= 0 , "Only Positive Number!"
        operation = input ("Enter the operation you would like to perform (+,-,*,/) or 'q to quit':")
        
        if operation == 'q':
            print("Goodbye!")
            break

        number2 = float( input("Enter Second number :"))
        assert number2 >= 0, "Only Positive Number!"

        if operation == '+':
             return number1+number2
        elif operation == '-':
             return number1-number2
        elif operation == '*':
             return number1*number2
        elif operation == '/':
            assert (number1/0), "Can't divide by zero"
            return number1/number2
        else:
             return "Invalid operation"
        print("Result:", result)
calculator()"""
#The main issue is that your calculator() function returns a result inside the loop,
# which exits the function after the first calculation.



