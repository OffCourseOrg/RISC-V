#!/bin/python3
from gdb_remote_client import GdbRemoteClient
import sys

from lib.architectures import riscv64 as arch
from lib import GDB
from lib import Objdump

####################################
port = int(sys.argv[1])
try:
  cli = GdbRemoteClient("localhost", port)
  cli.connect()
  gdb = GDB(cli, arch)

except:
  print(f"[ERROR] Server is not running on localhost:{port}")
  pass

try:
  obj_dump_path = sys.argv[2]
  obj = Objdump(obj_dump_path)
except:
  print("No Object Dump")
