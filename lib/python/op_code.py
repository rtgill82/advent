class OpCode:
    ADD  = 1
    MULT = 2
    IN   = 3
    OUT  = 4
    JNZ  = 5
    JZ   = 6
    STOL = 7
    STOE = 8
    HALT = 99

    MEM = 0
    IMM = 1

    def __init__(self, opcode):
        self._opcode, self._modes = self._deconstruct_opcode(opcode)
        self._size = self._op_size(opcode)

    def exec(self, ip, mem):
        switcher = {
            self.ADD:  self._add_op,
            self.MULT: self._mult_op,
            self.IN:   self._input,
            self.OUT:  self._output,
            self.JNZ:  self._jump_if_true,
            self.JZ:   self._jump_if_false,
            self.STOL: self._store_if_less,
            self.STOE: self._store_if_equal
        }
        func = switcher.get(self._opcode)
        return func(ip, mem)

    def opcode(self):
        return self._opcode

    def _deconstruct_opcode(self, code):
        opcode = code % 100
        modes = self._enum_modes(code)
        return (opcode, modes)

    def _enum_modes(self, code):
        digits = self._digits(code // 100)
        size = len(digits)
        digits = digits + [0 for i in range(3-len(digits))]
        return digits

    def _op_size(self, code):
        switcher = {
            self.ADD:  4,
            self.MULT: 4,
            self.STOL: 4,
            self.STOE: 4,
            self.JZ:   3,
            self.JNZ:  3,
            self.IN:   2,
            self.OUT:  2,
            self.HALT: 1
        }
        return switcher.get(code)

    def _read_operands(self, ip, mem):
        return mem[ip+1:self._size+ip]

    def _add_op(self, ip, mem):
        self._modes[2] = self.IMM
        val1, val2, addr = self._load_operands(ip, mem)
        mem[addr] = val1 + val2
        return ip + self._size

    def _mult_op(self, ip, mem):
        self._modes[2] = self.IMM
        val1, val2, addr = self._load_operands(ip, mem)
        mem[addr] = val1 * val2
        return ip + self._size

    def _input(self, ip, mem):
        val = int(input('? '))
        operand = self._read_operands(ip, mem)[0]
        mem[operand] = val
        return ip + self._size

    def _output(self, ip, mem):
        print(self._load_operands(ip, mem)[0])
        return ip + self._size

    def _jump_if_true(self, ip, mem):
        val, addr = self._load_operands(ip, mem)
        return ip + self._size if val == 0 else addr

    def _jump_if_false(self, ip, mem):
        val, addr = self._load_operands(ip, mem)
        return addr if val == 0 else ip + self._size

    def _store_if_less(self, ip, mem):
        self._modes[2] = self.IMM
        val1, val2, addr = self._load_operands(ip, mem)
        mem[addr] = 1 if val1 < val2 else 0
        return ip + self._size

    def _store_if_equal(self, ip, mem):
        self._modes[2] = self.IMM
        val1, val2, addr = self._load_operands(ip, mem)
        mem[addr] = 1 if val1 == val2 else 0
        return ip + self._size

    def _load_operands(self, ip, mem):
        ops = self._read_operands(ip, mem)
        fn = lambda item: mem[item[0]] if item[1] == self.MEM else item[0]
        return list(map(fn, zip(ops, self._modes)))

    def _digits(self, num):
        digits = []
        div = 10
        while num > 0:
            digits.append(num % div)
            num //= div
            div *= 10
        return digits

    def __eq__(self, other):
        if other.__class__ == OpCode:
            return self._opcode == other.opcode()
        elif other.__class__ == int:
            return self._opcode == other

    def __ne__(self, other):
        if other.__class__ == OpCode:
            return self._opcode != other.opcode()
        elif other.__class__ == int:
            return self._opcode != other
