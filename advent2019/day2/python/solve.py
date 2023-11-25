#!/usr/bin/python
from pathlib import Path
import sys

LIB_PATH = str(Path(__file__).parent.absolute().joinpath('../../lib/python'))
sys.path.append(LIB_PATH)
from intcode import IntcodeCPU

DATA = Path(__file__).parent.absolute().joinpath('../data/input.txt')
CPU_RESULT = 19690720

cpu = IntcodeCPU(DATA)
cpu.patch(0x01, 0x0c)
cpu.patch(0x02, 0x02)
result = cpu.run()
print(f"CPU return value for input 1202: {result}")

noun, verb = cpu.run_expect(CPU_RESULT)
input = 100 * noun + verb
print(f"CPU input for {CPU_RESULT}: {input}")
