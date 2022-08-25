def calculation():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    num1 = float(input("Enter a number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter an operation from the list above: ")
        num2 = float(input("Enter a number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        restart = input(
            f"Type 'y' if you want to continue with {answer}, otherwise type 'n' to start a new calculation: ")
        if restart == "y":
            num1 = answer
            should_continue = True

        elif restart == "n":
            should_continue = False
            calculation()


calculation()
