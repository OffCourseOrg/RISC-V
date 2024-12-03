SOURCE=counter.s
RISCV_PATH=/opt/riscv
RISCV_BIN=$(RISCV_PATH)/bin

all: counter

counter: $(SOURCE)
	rm -rf 
	$(RISCV_BIN)/riscv64-unknown-elf-as $< -o counter.o
	$(RISCV_BIN)/riscv64-unknown-elf-ld counter.o -o $@
	rm counter.o

run: counter
	$(RISCV_BIN)/qemu-riscv64-static -g 1235 $<
