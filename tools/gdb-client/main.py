#!/bin/python3
from gdb_remote_client import GdbRemoteClient
import sys

ARCH = 64;          #bits
WL = int(ARCH / 8); #bytes
HL = int(WL / 2);   #bytes
DW = int(WL * 2);   #bytes
QL = int(WL * 4);   #bytes
BIN_LEN = ARCH
HEX_LEN = int(BIN_LEN / 4);

regs = {
    "zero": 0, "ra": 0, "sp": 0, "gp": 0, "tp": 0, "t0": 0, "t1": 0, "t2": 0, 
    "fp": 0, "s1": 0, "a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, 
    "a6": 0, "a7": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0, "s7": 0, 
    "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0, "pc": 0
}
REG_LEN = len(regs)

def fixEndian(buffer):
    buffer = reverse(buffer)
    buf = ""
    for i in range(0, len(buffer), 2):
        buf += buffer[i+1]
        buf += buffer[i]
    return buf;

def next(amount = 1):
    for _ in range(amount):
        cli.cmd("vCont;s")

def chop_str(string, size):
    return [string[0:int(size)], string[int(size)::]]


def p_regs(fetch = 0, keys = []):
    if (fetch):
        r_regs();
    for key in regs:
        if(keys != [] and key not in keys):
            continue
        print(f"{key:>4}:", end="")
        print(hex(regs[key]))


def reverse(string):
    return string[::-1]

def r_regs():
    regs_s = cli.cmd("g")
    for key in regs:
        [t, regs_s] = chop_str(regs_s, HEX_LEN)
        t = fixEndian(t);
        regs[key] = int(f"0x{t}", 16)


####################################
port = int(sys.argv[1])
try:
    cli = GdbRemoteClient("localhost", port)

    cli.connect();
except:
    print(f"[ERROR] Server is not running on localhost:{port}")
    pass


    port = int(sys.argv[1])
