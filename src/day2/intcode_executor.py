
def add(x :int,y: int):
    return x + y

def multiply(x :int,y: int):
    return x * y

def operation(v):
    operations = {
        1: add,
        2: multiply
        }
    return operations.get(v, "Invalid operation")

def execute(memory : [int]):
    instruction_pointer = 0
    while memory[instruction_pointer] != 99:
        op = operation(memory[instruction_pointer])
        address_of_first_parameter = memory[instruction_pointer + 1]
        address_of_second_parameter = memory[instruction_pointer + 2]
        operation_result = op(memory[address_of_first_parameter], memory[address_of_second_parameter])
        result_address = memory[instruction_pointer + 3]
        memory[result_address] = operation_result
        instruction_pointer = instruction_pointer + 4
    return memory

def restore_from_before_fire_and_execute(memory : [int]):
    memory[1] = 12
    memory[2] = 2
    return execute(memory)

def set_noun_and_verb_and_execute(memory :[int], noun :int, verb :int):
    memory[1] = noun
    memory[2] = verb
    return execute(memory)

def day_two_solution(memory :[int]):
    for n in range(0, 99):
        for v in range(0, 99):
            try:
                if(set_noun_and_verb_and_execute(memory.copy(), n, v)[0] == 19690720):
                    return [n, v]
            except:
                "noop"
    return "something went wrong"