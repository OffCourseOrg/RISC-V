#!/bin/python3
from gdb_remote_client import GdbRemoteClient
import sys

from lib.architectures import riscv64 as arch
from lib import GDB, utils

####################################
port = int(sys.argv[1])
try:
    cli = GdbRemoteClient("localhost", port)
    cli.connect()

except:
    print(f"[ERROR] Server is not running on localhost:{port}")
    pass

gdb = GDB(cli, arch)