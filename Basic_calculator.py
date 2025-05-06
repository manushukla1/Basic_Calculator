import math

def calculator():
    while True:
        try:
            print("\nSimple Calculator")
            number1 = float(input("Enter first number: "))
            assert number1 >= 0, "Only positive numbers allowed."

            operation = input("Enter the operation (+, -, *, /, ** for power, sqrt for square root, or 'q' to quit): ")

            if operation == 'q':
                print("Goodbye!")
                break

            # Square root is a single-input operation
            if operation == 'sqrt':
                result = math.sqrt(number1)
            else:
                number2 = float(input("Enter second number: "))
                assert number2 >= 0, "Only positive numbers allowed."

                if operation == '+':
                    result = number1 + number2
                elif operation == '-':
                    result = number1 - number2
                elif operation == '*':
                    result = number1 * number2
                elif operation == '/':
                    assert number2 != 0, "Cannot divide by zero!"
                    result = number1 / number2
                elif operation == '**':
                    result = number1 ** number2
                else:
                    print("Invalid operation.")
                    continue

            print("Result:", result)

        except ValueError:
            print("❌ Please enter valid numbers.")
        except AssertionError as ae:
            print("❌", ae)
        except ZeroDivisionError as zde:
            print("❌", zde)
        except Exception as e:
            print("Unexpected error:", e)

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



