# *
# *  OffCourse::RISC-V
# *		-GDB Client Library
# *
# *  Written by: Sybe
# *  License: MIT
# *

def reverse(string):
    return string[::-1]

#It's hilarius this is the best solution
def chop_str(string, size):
    return [string[0:int(size)], string[int(size)::]]

def hex2str(num, include_0x=0):
    if (include_0x):
        return hex(num)
    return hex(num)[2::]

def fixEndian(buffer):
    buffer = reverse(buffer)
    buf = ""
    for i in range(0, len(buffer), 2):
        buf += buffer[i+1]
        buf += buffer[i]
    return buf;