# RISC-V jail environment
This repo has offcourse's RISC-V jail implementation

## Installation
Dependencies [qemu-user-static](https://github.com/multiarch/qemu-user-static), [RISC-V-gnu-toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain)

Install `qemu-static` RISC-V64 version
```
wget https://github.com/multiarch/qemu-user-static/releases/download/v7.2.0-1/qemu-riscv64-static
sudo mv qemu-riscv64-static /bin
```
Install RISC-V-gnu-toolchain with Newlib. All toolchain will be installed in path set in `$RISCV_PATH` variable. Later you can add `$RISCV_PATH` to your `$PATH` variable or link needed executables to `/bin`.
```
git clone --detph=1 https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain
RISCV_PATH=/opt/riscv/
./configure --prefix=$RISCV_PATH
make -j[number-of-threads] #it takes long time to build, so do not be greedy on threads
```
## Usage
To compile and run c program
```
$RISCV_PATH/bin/riscv64-unknown-elf-gcc -static -o main main.c
qemu-riscv64-static ./main
# OUTPUT: Hello world
```
Compile assembly 
```
$RISCV_PATH/bin/riscv64-unknown-elf-as -o main.o main.s
$RISCV_PATH/bin/riscv64-unknown-elf-gcc -o main main.o
qemu-riscv64-static ./main
# OUTPUT: Hello world
```
For debugging with gdb
```
$RISCV_PATH/bin/riscv64-unknown-elf-gcc -static -ggdb -o main main.c
qemu-riscv64-static -g <port> ./main

#in different terminal
$RISCV_PATH/riscv64-unknown-elf-gdb main
(gdb) target remote localhost:<port>
(gdb) break main #or any other point
(gdb) continue
```
## Useful resourses
- [RISC-V gdb tutorial](https://shakti.org.in/docs/RISC-V-GDB-tutorial.pdf)
- [RISC-V calling convention](https://riscv.org/wp-content/uploads/2015/01/riscv-calling.pdf)
- [pk syscall.h file](https://github.com/riscv-software-src/riscv-pk/blob/master/pk/syscall.h)
