import operator
import os

BORDER_LENGTH = 30
BORDER_CHAR = "="
OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def restart_program(message):
    print(20*"\n")
    if message:
        print(get_border(), end="\n")
        print(message)
        print(get_border(), end="\n")
    main()


def get_border():
    return "=" * BORDER_LENGTH


def get_header():
    return (
        "              .__\n"
        "  ____ _____  |  |   ____\n"
        "_/ ___\\\\__  \\ |  | _/ ___\\\n"
        "\\  \\___ / __ \\|  |_\\  \\___\n"
        " \\___  >____  /____/\\___  >\n"
        "     \\/     \\/          \\/\n")


def print_welcome():
    print(get_header(), end="\n")
    print(get_border(), end="\n")


def can_cast_to_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def read_operand(side):
    raw_str = input(side + " Operand: ")

    if not can_cast_to_float(raw_str):
        restart_program(f"Couldn't cast operand ('{raw_str}') to a float value!")

    return raw_str


def read_operator():
    operator_input = input("Operation: ")
    hit = False

    for op in OPERATORS.keys():
        if operator_input == op:
            hit = True

    if not hit:
        restart_program(f"Operator ('{operator_input}') not in the list of Operants!")

    return operator_input


def main():
    print_welcome()

    left_operand = read_operand("left")
    right_operand = read_operand("right")
    operation = read_operator()

    result = OPERATORS[operation](float(left_operand), float(right_operand))
    print(result)

    if input("Again?: "):
        restart_program("")


if __name__ == "__main__":
    main()
