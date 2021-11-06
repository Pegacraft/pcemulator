text: str = ""


def get_input():
    input_val: str = input("Input: ")
    try:
        return int(input_val, 2)
    except ValueError:
        pass
    try:
        return int(input_val, 10)
    except ValueError:
        pass
    try:
        return int(input_val, 16)
    except ValueError:
        pass


def get_output(value: int):
    print(value)
    print(chr(value))


def string_append(value: int):
    global text
    text += chr(value)


def string_clear():
    global text
    text = ""


def string_send():
    print(text)
