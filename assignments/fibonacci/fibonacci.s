.data
str1:    .asciz "Input number: "
str2:    .asciz "result = "

.section .text

.global main
main:
  addi sp, sp, -4
  sw ra, 0(sp)
  la a0, str1
  call print_string

	call read_int

  call fibonacci

  mv s1, a0
  la a0,str2
  call print_string

  mv a0,s1
  call print_int

	call exit
  ret
 
fibonacci:
  addi sp, sp, -16 # 12:ra, 8:k, 4:a, 0:b
  sw ra, 12(sp)
  sw a0, 8(sp) # k
  li t0, 1
  beq a0, zero, Return
  beq a0, t0, Return

  lw a0, 8(sp) # get k
  addi a0, a0, -1
  call fibonacci # a in a0
  sw a0, 4(sp) # saved a

  lw a0, 8(sp) # get k
  addi a0, a0, -2
  call fibonacci # b in a0
  sw a0, 0(sp) # save b

  lw t1, 0(sp) # get b
  lw t2, 4(sp) # get a
  add a0, t1, t2
  lw ra, 12(sp)
  addi sp, sp, 16 # clean the stack
  ret

Return:
  lw ra, 12(sp)
  addi sp, sp, 16
  li a0, 1
  ret

