# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandrs
# *  License: MIT
# *

from . import utils

class Memory:
  def __init__(self, gdb):
    self.gdb = gdb
    self.mem = {}
    self.root_sp = self.gdb.registers.regs["sp"];

  def set_root_sp(self, root_sp):
      self.root_sp = root_sp

# We always fetch the whole stack, because we can. 
  def fetch(self, force = False):
    if not self.gdb.registers.fetched or force:
      self.gdb.registers.fetch()

    sw = self.gdb.arch.single_word;
    current_sp = self.gdb.registers['sp'];
    for addr in range(self.root_sp, current_sp, -sw):
        m = self.gdb.cli.cmd(f"m {utils.hex2str(addr)},{sw}")
        self.mem[addr] = int(utils.fixEndian(m), 16)

  def print(self):
    for key in self.mem:
        utils.print_hex(key, self.gdb.arch.hex, end=': ');
        utils.print_hex(self.mem[key], self.gdb.arch.hex);

  def print_normalised(self):
    for key in self.mem:
        utils.print_hex(key - self.root_sp, self.gdb.arch.hex, end=': ');
        utils.print_hex(self.mem[key], self.gdb.arch.hex);
