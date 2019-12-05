from enum import Enum

class Op(Enum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    STOP = 99

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1

class IntCode:
    def __init__(self, memory, input_fn=None, output_fn=print):
        self.instruction_pointer = 0
        self.memory = list(memory)
        self.input_fn = input_fn
        self.output_fn = output_fn

    def next_instruction(self):
        instruction = self.memory[self.instruction_pointer]
        self.instruction_pointer += 1
        return instruction

    def get_parameter_value(self):
        mode = Mode(self.modes % 10)
        self.modes //= 10
        ivalue = self.next_instruction()
        if mode == Mode.POSITION:
            return self.memory[ivalue]
        elif mode == Mode.IMMEDIATE:
            return ivalue

    def set_at_parameter(self, value):
        self.memory[self.next_instruction()] = value

    def operation(self, v):
        operations = {
            Op.ADD: lambda: self.set_at_parameter(self.get_parameter_value() + self.get_parameter_value()),
            Op.MUL: lambda:  self.set_at_parameter(self.get_parameter_value() * self.get_parameter_value()),
            Op.INPUT: lambda: self.set_at_parameter(self.input_fn()),
            Op.OUTPUT: lambda: self.output_fn(self.get_parameter_value()),
            Op.JUMP_IF_TRUE: lambda: (
                val := self.get_parameter_value(),
                where := self.get_parameter_value(),
                self.instruction_pointer := where if val != 0 else True),
            Op.JUMP_IF_FALSE: lambda: (
                val := self.get_parameter_value(),
                where := self.get_parameter_value(),
                self.instruction_pointer := where if val == 0 else True),
            Op.EQUALS: lambda: self.set_at_parameter(int(self.get_parameter_value() == self.get_parameter_value())),
            Op.LESS_THAN: lambda: self.set_at_parameter(int(self.get_parameter_value() < self.get_parameter_value())),
            Op.STOP: lambda: False
        }
        return operations.get(v, lambda: True)

    def step(self):
        instruction = self.next_instruction()
        opcode = Op(instruction % 100)
        self.modes = instruction // 100
        op = operation(opcode)
        if op() == False:
            return False
        return True

    def run(self):
        while self.step():
            pass

def read_input():
    with open("src/day5/input.txt") as f:
        return [int(v) for v in f.read().split(",")]

class TestableIntCode(IntCode):
    def __init__(self, memory, inputs):
        self.inputs = list(reversed(inputs))
        self.outputs = []
        super().__init__(memory, input_fn=self.inputs.pop, output_fn=self.outputs.append)

