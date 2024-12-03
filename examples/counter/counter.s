.text
.global _start

_start:
  mv a0, zero
  
function_increment:
  addi a0, a0, 1

  addi sp, sp, -8
  sd a0,0(sp)
  j function_increment 


