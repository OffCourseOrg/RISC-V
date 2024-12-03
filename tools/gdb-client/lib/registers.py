# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandres
# *  License: MIT
# *

from . import utils

class Registers:
  def __init__(self, gdb):
    self.gdb = gdb
    self.regs = {
      "zero": 0x0, "ra": 0x0, "sp": 0x0, "gp": 0x0, "tp": 0x0, "t0": 0x0, "t1": 0x0, "t2": 0x0, 
      "fp": 0x0, "s1": 0x0, "a0": 0x0, "a1": 0x0, "a2": 0x0, "a3": 0x0, "a4": 0x0, "a5": 0x0, 
      "a6": 0x0, "a7": 0x0, "s2": 0x0, "s3": 0x0, "s4": 0x0, "s5": 0x0, "s6": 0x0, "s7": 0x0, 
      "s8": 0x0, "s9": 0x0, "s10": 0x0, "s11": 0x0, "t3": 0x0, "t4": 0x0, "t5": 0x0, "t6": 0x0, "pc": 0x0
    }
    self.fetch()

  def __getitem__(self, key):
    return self.regs[key]

  def __iter__(self):
    return self.regs.keys()

  def fetch(self):
    hex_string = self.gdb.cli.cmd("g")
    for key in self.regs:
      [t, hex_string] = utils.chop_str(hex_string, self.gdb.arch.hex)
      t = utils.fixEndian(t)
      self.regs[key] = int(f"0x{t}", 16)

  def print(self, keys=[]):
    for key in self.regs:
        if(keys != [] and key not in keys):
            continue
        print(f"{key:<4}:", hex(self.regs[key]))

  def values(self):
    return self.regs.values()

  def items(self):
    return self.regs.items()

  def len(self):
    len(self.regs)
