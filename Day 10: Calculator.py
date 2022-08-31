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


def calculator():
    n1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation from the list above: ")
        n2 = int(input("What's the next number?: "))

        operation_function = operations[operation_symbol]
        answer = operation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        continue_calculating = input(
            f"Type 'y' to continue with {answer}, otherwise type 'n' to start a new calculation: ")

        if continue_calculating == 'y':
            n1 = answer

        else:
            should_continue = False
            calculator()


calculator()
