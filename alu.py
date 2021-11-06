def op_add(val1: int, val2: int):
    return val1 + val2


def op_subtract(val1: int, val2: int):
    return val1 - val2


def op_and(val1: int, val2: int):
    return val1 & val2


def op_or(val1: int, val2: int):
    return val1 | val2


def op_not(val1: int):
    return ~val1


def op_xor(val1: int, val2: int):
    return val1 ^ val2


def interpret(opcode: int, val1: int, val2: int):
    if opcode == 0b0000_0001:
        return op_add(val1, val2)
    elif opcode == 0b0000_0010:
        return op_subtract(val1, val2)
    elif opcode == 0b0000_0011:
        return op_and(val1, val2)
    elif opcode == 0b0000_0100:
        return op_or(val1, val2)
    elif opcode == 0b0000_0101:
        return op_not(val1)
    elif opcode == 0b0000_0110:
        return op_xor(val1, val2)
