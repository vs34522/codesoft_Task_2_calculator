def input_number():
    a = input("Enter a number: ")
    b = input("Enter another number: ")

    def calculate_twonumbers(a, b):
        a = float(a)
        b = float(b)

        c = input("Enter an operation (+, -, *, /): ")
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        elif c == '/':
            if b != 0:
                return a / b
            else:
                return "❌ Division by zero is not allowed."
        else:
            return "❌ Invalid operation."

    result = calculate_twonumbers(a, b)
    print("Result:", result)

# Call the function to run the calculator
input_number()
