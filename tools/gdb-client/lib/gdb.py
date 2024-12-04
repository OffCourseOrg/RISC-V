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
    self.registers.fetch()
    self.memory = Memory(self)
    self.memory.fetch()

  def next(self, steps=1, fetch = False):
    self.registers.fetched = False;
    for _ in range(steps):
      self.cli.cmd("vCont;s")
    if fetch:
        self.fetch()

  def fetch(self):
    self.registers.fetch()
    self.memory.fetch()
