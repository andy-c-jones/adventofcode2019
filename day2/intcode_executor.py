
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

def execute(command : [int]):
    execution_pointer = 0
    while command[execution_pointer] != 99:
        op = operation(command[execution_pointer])
        positionOfFirstOpperand = command[execution_pointer + 1]
        positionOfSecondOpperand = command[execution_pointer + 2]
        resultOfOpperation = op(command[positionOfFirstOpperand], command[positionOfSecondOpperand])
        locationOfResult = command[execution_pointer + 3]
        command[locationOfResult] = resultOfOpperation
        execution_pointer = execution_pointer + 4
    return command

def restore_from_before_fire_and_execute(command : [int]):
    command[1] = 12
    command[2] = 2
    return execute(command)

