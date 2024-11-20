.data
str: .ascii "Hello world\n"

.text
.global main


main:

  li a0, 1
  la a1, str
  li a2, 12
  li a7, 64
  ecall

  li a0, 0 # exit code 
  li a7, 93 # SYS_exit
  ecall

