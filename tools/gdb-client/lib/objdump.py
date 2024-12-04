# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Aleksandrs
# *  License: MIT
# *

from . import utils
from .architectures import riscv64, riscv32

class Objdump:
  def __init__(self, path):
    self.labels = {}
    self.instuctions = {}
    code_found = False;
    with open(path, "r") as file:
      for line in file:
        if not hasattr(self, 'arch'):
          if 'elf64' in line:
            self.arch = riscv64
          if 'elf32' in line:
            self.arch = riscv32
        if "section .text:" in line:
          code_found = True
          continue; # skipping one cicle to code

        if not code_found or line.strip() == '':
          continue;

        if ">:" in line: #means a lable
          [value, key] = line.split()
          key = key[1:]
          key = key[:-2]
          self.labels[key] = int(value, 16);
        else:## it is an instruction
          [key, value] = line.split(':')
          key = int(key.strip(), 16)
          value.strip()
          tokens = value.split()[1:]
          value = tokens[0]
          tokens = tokens[1:]
          if '<' in ''.join(tokens):
            label = tokens[-1]
            label = label[1:]
            label = label[:1]
            tokens = tokens[:-2]
            tokens.append(label)
          value+=' '  
          value += ', '.join(tokens)
          self.instuctions[key] = value

  def print_instructions(self, keys=[]):
    for key in self.instuctions:
      if(keys != [] and key not in keys):
          continue
      utils.print_hex(key, self.arch.hex, end=': ')
      print(f"{self.instuctions[key]}")

         
  def print_labels(self, keys=[]):
    for key in self.labels:
      if(keys != [] and key not in keys):
          continue
      print(f"{key}: ", end='')
      utils.print_hex(self.labels[key], self.arch.hex)





