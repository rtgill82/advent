from op_code import OpCode

class IntcodeCPU:
    def __init__(self, data):
        self._data = self._read_file(data)
        self.reset()

    def reset(self):
        self._ip = 0
        self._mem = self._data.copy()

    def run(self):
        opcode = OpCode(self._mem[self._ip])
        while opcode != OpCode.HALT:
            self._ip = opcode.exec(self._ip, self._mem)
            opcode = OpCode(self._mem[self._ip])
        return self._mem[0]

    def run_expect(self, value):
        for noun in range(0, 99):
            for verb in range(0, 99):
                self.reset()
                self.patch(0x01, noun)
                self.patch(0x02, verb)
                if self.run() == value: return (noun, verb)

    def patch(self, addr, value):
        self._mem[addr] = value

    def _read_file(self, path):
        with open(path, 'r') as file:
            contents = file.read()
            return list(map(int, contents.rstrip().split(',')))
