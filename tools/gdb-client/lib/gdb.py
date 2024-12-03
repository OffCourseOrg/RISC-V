# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Sybe
# *  License: MIT
# *

from .registers import Registers
from .memory import Memory

class GDB:
  def __init__(self, cli, arch):
    self.cli = cli
    self.arch = arch
    self.registers = Registers(self)
    self.memory = Memory(self)

  def next(self, steps=1):
    for _ in range(steps):
      self.cli.cmd("vCont;s")