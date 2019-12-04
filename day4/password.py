def find_password_in_range(min:int, max:int):
    return sum(int(is_valid_password_part_1(n)) for n in range(min, max))

def is_valid_password_part_1(n):
    s = str(n)
    has_pair = any(a == b for a, b in zip(s, s[1:]))
    goes_up = all(a <= b for a, b in zip(s, s[1:]))
    return has_pair and goes_up

def find_password_in_range_part2(min:int, max:int):
    return sum(int(is_valid_password_part_2(n)) for n in range(min, max))

def is_valid_password_part_2(n):
    s = str(n)
    sp = " " + s + " "
    has_pair = any(a != b == c != d for a, b, c, d in zip(sp, sp[1:], sp[2:], sp[3:]))
    goes_up = all(a <= b for a, b in zip(s, s[1:]))
    return has_pair and goes_up
    
