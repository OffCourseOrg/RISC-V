# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandres
# *  License: MIT
# *

from . import utils

class Memory:
  def __init__(self, gdb):
    self.gdb = gdb
    self.mem = {}

  def read_frame(self):
    if self.gdb.registers['sp'] == 0:
      self.gdb.registers.fetch()
    m = self.gdb.cli.cmd(f"m {utils.hex2str(self.gdb.registers['sp'])},{self.gdb.arch.single_word}")
    self.mem[self.gdb.registers['sp']] = int(utils.fixEndian(m))

  def print(self):
    for key in self.mem:
        print(f"{hex(key)}: {hex(self.mem[key])}")