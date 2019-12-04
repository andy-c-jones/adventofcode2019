def parse(wire):
    directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
    for move in wire.split(","):
        direction = move[0]
        distance = int(move[1:])
        yield directions[direction], distance

def coordinates_wire_covers(wire):
    x, y = 0, 0
    for (dx, dy), distance in parse(wire):
        for _ in range(distance):
            x += dx 
            y += dy
            yield x, y

def where_wires_touch(one, two):
    return set(coordinates_wire_covers(one)) & set(coordinates_wire_covers(two))

def closest_place_wires_touch(one, two):
    return min(abs(x) + abs(y) for x, y in where_wires_touch(one, two))

def coordinates_wire_covers_with_steps_to_get_there(wire):
    x, y, steps = 0, 0, 0
    for (dx, dy), distance in parse(wire):
        for _ in range(distance):
            x += dx; y += dy; steps += 1
            yield x, y, steps

def step_map(wire):
    return {(x, y): steps for x, y, steps in coordinates_wire_covers_with_steps_to_get_there(wire)}

def fewest_steps_to_wire_touching(one, two):
    map_one = step_map(one)
    map_two = step_map(two)
    where_wires_touch = set(map_one) & set(map_two)
    return min(map_one[p] + map_two[p] for p in where_wires_touch)
