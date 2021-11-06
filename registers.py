import counter

registers: dict = {}


def reg_write(value: int, opcode: int):
    if value is None:
        return
    if opcode == 0b1111_0111:
        counter.set_counter(value)
    elif opcode == 0b1111_1000:
        registers[0] = value
    elif opcode == 0b1111_1001:
        registers[1] = value
    elif opcode == 0b1111_1010:
        registers[2] = value
    elif opcode == 0b1111_1011:
        registers[3] = value
    elif opcode == 0b1111_1100:
        registers[4] = value
    elif opcode == 0b1111_1101:
        registers[5] = value
    elif opcode == 0b1111_1110:
        registers[6] = value
    elif opcode == 0b1111_1111:
        print(value)


def reg_read(opcode: int):
    if opcode == 0b1111_0111:
        return counter.get_current()
    elif opcode == 0b1111_1000:
        return registers.get(0)
    elif opcode == 0b1111_1001:
        return registers.get(1)
    elif opcode == 0b1111_1010:
        return registers.get(2)
    elif opcode == 0b1111_1011:
        return registers.get(3)
    elif opcode == 0b1111_1100:
        return registers.get(4)
    elif opcode == 0b1111_1101:
        return registers.get(5)
    elif opcode == 0b1111_1110:
        return registers.get(6)
    elif opcode == 0b1111_1111:
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
    else:
        return opcode
