import math
history = [] # store each calculation in a list and display it on demand.
memory = None      # we can set it as zero but here i have taken it as None and for handling None i have added checks while assigning value
def calculator():
    while True:
        try:
            print("\nSimple Calculator with Memory")
            inp1 = input("Enter first number (or 'm'): ")
            if inp1.lower()== 'm' and memory is not None:
                    number1 = memory  # Use memory if available
            elif inp1.lower()== 'm' and memory is  None:
                print("❌ No memory available.")
                continue
            else:
               number1 = float(inp1)
               assert number1 >= 0, "Only positive numbers allowed!"

            # operation block
            operation = input("Enter the operation (+, -, *, /, ** for power, sqrt for square root, or 'q' to quit or 'h' for history): ")
            if operation == 'q':
                print("Goodbye!")
                break
            elif operation == 'h':
                print("\n Records")
                for record in history:
                    print(record)
                continue
            # Square root is a single-input operation
            elif operation == 'sqrt':
                result = math.sqrt(number1)
            else:
                inp2 = input("Enter Second number (or 'm'): ")
                if inp2.lower() == 'm' and memory is not None:
                    number2 = memory  # Use memory if available
                elif inp2.lower() == 'm' and memory is None:
                    print("❌ No memory available.")
                    continue
                else:
                    number2 = float(inp2)
                    assert number2 >= 0, "Only positive numbers allowed!"

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

                history.append (f"{number1} {operation} {number2} = {result}")
                print("Result:", result)
                memory = result
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



