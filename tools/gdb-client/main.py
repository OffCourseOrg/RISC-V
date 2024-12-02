#!/bin/python3
from gdb_remote_client import GdbRemoteClient
import sys

BITS = 64;

regs = {
    "zero": 0, "ra": 0, "sp": 0, "gp": 0, "tp": 0, "t0": 0, "t1": 0, "t2": 0, 
    "fp": 0, "s1": 0, "a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, 
    "a6": 0, "a7": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0, "s7": 0, 
    "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0, "pc": 0
}

def endianFix(val):
        buf = "";
        for i in range(0, len(val), 2):
            buf += regs[key][i+1] + regs[key][i]
        return buf

def p_bytes(val = ""):
    for i in range(len(val) / (BITS/8)):
        print((regs_t[i*16:16*i+16])[::-1])

def read_regs():
    regs_t = cli.cmd("g")
    for i, key in enumerate(regs):
        regs[key] = (regs_t[i*16:16*i+16])[::-1]

    for key in regs:
        regs[key] = endianFix(regs[key])

def print_regs(fetch = 0, keys = []):
    if(fetch):
        read_regs()
    for key in regs:
        if(keys != []):
            if(key in keys):
                print('{:>4}:'.format(key), regs[key])
        else:
            print('{:>4}:'.format(key), regs[key])


def next(amount = 1):
    for i in range(amount):
        cli.cmd("vCont;s")

cli = GdbRemoteClient("localhost", int(sys.argv[1]))

cli.connect();

