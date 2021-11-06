ram: dict = {}


def ram_write(value: int, address: int):
    ram[address] = value


def ram_read(address: int):
    return ram.get(address)


def interpret(opcode: int, value1: int, value2: int):
    if opcode == 0b0001_0011:
        ram_write(value1, value2)
    elif opcode == 0b0001_0100:
        return ram_read(value1)
