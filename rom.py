rom: dict = {}


def rom_write(opcode: int, address: int):
    rom[address] = opcode


def rom_write4(opcode: tuple, address: int):
    rom[address] = opcode[0]
    rom[address + 1] = opcode[1]
    rom[address + 2] = opcode[2]
    rom[address + 3] = opcode[3]


def rom_read(address: int):
    return rom.get(address)


def rom_read4(address: int):
    return rom.get(address), rom.get(address + 1), rom.get(address + 2), rom.get(address + 3)
