# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandrs
# *  License: MIT
# *

# // is intiger division
class Architecture:
  def __init__(self, name="empty", bits=0):
    self.name = name
    self.bits = bits  #bits
    self.hex = bits // 4
    self.single_word    = bits // 8;    #bytes
    self.half_word      = bits // 16;   #bytes
    self.double_word    = self.single_word * 2; #bytes
    self.quadruple_word = self.single_word * 4; #bytes

  def print(self):
      print(self.name)
      print(f"Bits per instruction: {self.bits}")
      print(f"Single word length in bytes: {self.single_word}")
      print(f"Half word length in bytes: {self.half_word}")
      print(f"Double word length in bytes: {self.double_word}")
      print(f"Quadruple word length in bytes: {self.quadruple_word}")

riscv64 = Architecture("riscv64", 64)
riscv32 = Architecture("riscv32", 32)
