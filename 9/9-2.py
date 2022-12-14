movement_map = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}


def step(x):
    if x > 1:
        return 1
    elif x < -1:
        return -1
    else:
        return x


def move_next_knot(knot_pos, next_knot_pos):
    next_knot_dx, next_knot_dy = knot_pos[0] - \
        next_knot_pos[0], knot_pos[1] - next_knot_pos[1]
    next_knot_x, next_knot_y = next_knot_pos[0], next_knot_pos[1]

    if abs(next_knot_dx) > 1 or abs(next_knot_dy) > 1:
        next_knot_x, next_knot_y = next_knot_x + \
            step(next_knot_dx), next_knot_y + step(next_knot_dy)

    return (next_knot_x, next_knot_y)


with open('./9/input.txt') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')
    movements = list(map(lambda line: line.split(' '), lines))

knots_pos = [(0, 0) for _ in range(10)]
tail_visited_positions = {(0, 0): True}
for direction, amount in movements:
    for _ in range(int(amount)):
        head_knot_dx, head_knot_dy = movement_map[direction]
        head_knot_x, head_knot_y = knots_pos[0][0] + \
            head_knot_dx, knots_pos[0][1] + head_knot_dy
        knots_pos[0] = (head_knot_x, head_knot_y)

        for i in range(0, len(knots_pos) - 1):
            knots_pos[i+1] = move_next_knot(knots_pos[i], knots_pos[i+1])
        tail_visited_positions[knots_pos[-1]] = True

print(len(tail_visited_positions.keys()))
