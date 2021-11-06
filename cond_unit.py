def interpret(opcode: int, value1: int, value2: int):
    if opcode == 0b0000_0111:
        return value1 == value2
    elif opcode == 0b0000_1000:
        return value1 != value2
    elif opcode == 0b0000_1001:
        return value1 < value2
    elif opcode == 0b0000_1010:
        return value1 <= value2
    elif opcode == 0b0000_1011:
        return value1 > value2
    elif opcode == 0b0000_1100:
        return value1 >= value2
    elif opcode == 0b0000_1101:
        return True
    elif opcode == 0b0000_1110:
        return False
