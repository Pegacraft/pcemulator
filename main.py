import alu
import cond_unit
import counter
import ram
import registers
import rom

if __name__ == '__main__':
    rom.rom_write4((19, 1, 0, None), 0)
    rom.rom_write4((20, 0, 249, None), 3)
    rom.rom_write4((1, 249, 0, 255), 6)

    while True:
        # Translates the instruction into a usable form
        instruction: tuple = rom.rom_read4(counter.get_current())
        instruction_translated: list = list(instruction)

        instruction_translated[1] = registers.reg_read(instruction[1])
        instruction_translated[2] = registers.reg_read(instruction[2])

        # does the alu operations
        if instruction_translated[0] == 0b0000_0101:
            registers.reg_write(
                alu.interpret(instruction_translated[0], instruction_translated[1], instruction_translated[2]),
                instruction[2])
        else:
            registers.reg_write(
                alu.interpret(instruction_translated[0], instruction_translated[1], instruction_translated[2]),
                instruction[3])

        # does the conditional operations
        if cond_unit.interpret(instruction_translated[0], instruction_translated[1], instruction_translated[2]):
            counter.set_counter(instruction_translated[3])

        # does ram operations
        if ram.interpret(instruction_translated[0], instruction_translated[1], instruction_translated[2]) is not None:
            registers.reg_write(
                ram.interpret(instruction_translated[0], instruction_translated[1], instruction_translated[2]),
                instruction[2])
        # Increments the counter depending on the instruction
        if instruction_translated[0] is None:
            counter.increment(1)
        elif 0b0000_0001 <= instruction_translated[0] <= 0b0000_0110:
            if instruction_translated[0] == 0b0000_0101:
                counter.increment(3)
            else:
                counter.increment(4)
        elif 0b0000_0111 <= instruction_translated[0] <= 0b0000_1110 and not cond_unit.interpret(
                instruction_translated[0],
                instruction_translated[1],
                instruction_translated[
                    2]):
            counter.increment(4)
        elif instruction_translated[0] == 0b0001_0011 or 0b0001_0100:
            counter.increment(3)

        # Rom length
        if counter.get_current() == 255:
            break
