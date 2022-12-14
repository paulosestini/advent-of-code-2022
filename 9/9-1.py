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


def move_rope(head_pos, tail_pos, direction):
    head_dx, head_dy = movement_map[direction]
    head_x, head_y = head_pos[0] + head_dx, head_pos[1] + head_dy

    tail_dx, tail_dy = head_x - tail_pos[0], head_y - tail_pos[1]
    tail_x, tail_y = tail_pos[0], tail_pos[1]

    if abs(tail_dx) > 1 or abs(tail_dy) > 1:
        tail_x, tail_y = tail_x + step(tail_dx), tail_y + step(tail_dy)

    return (head_x, head_y), (tail_x, tail_y)


with open('./9/input.txt') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')
    movements = list(map(lambda line: line.split(' '), lines))

head_pos = (0, 0)
tail_pos = (0, 0)
tail_visited_positions = {(0, 0): True}
for direction, amount in movements:
    for _ in range(int(amount)):
        head_pos, tail_pos = move_rope(head_pos, tail_pos, direction)
        tail_visited_positions[tail_pos] = True

print(len(tail_visited_positions.keys()))
