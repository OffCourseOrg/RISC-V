# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandres
# *  License: MIT
# *


class Architecture:
  def __init__(self, name="empty", bits=0):
    self.name = name
    self.bits = bits  #bits
    self.hex = bits / 4
    self.single_word    = int(bits / 8);    #bytes
    self.half_word      = int(bits / 16);   #bytes
    self.double_word    = int(self.single_word * 2); #bytes
    self.quadruple_word = int(self.single_word * 4); #bytes

riscv64 = Architecture("riscv64", 64)
riscv32 = Architecture("riscv32", 32)