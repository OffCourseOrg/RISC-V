.text
.global _start

_start:
  mv a0, zero
  
function_increment:
  addi a0, a0, 1

  addi sp, sp, -32
  sd ra,24(sp)
  sd s0,16(sp)
  addi s0,sp,32

  sd a0,0(sp)
  j function_increment 


