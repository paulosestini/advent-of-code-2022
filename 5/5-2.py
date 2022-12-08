import re


def build_stacks(stack_lines: 'list[str]') -> 'list[list[str]]':
    stacks = [[] for _ in range(number_of_stacks)]

    for stack_line in stack_lines[::-1]:
        for i in range(number_of_stacks):
            if stack_line[1+4*i] != ' ':
                stacks[i].append(stack_line[1+4*i])
    return stacks


def move_items(stacks: 'list[list[int]]', movement_line: str):
    n_items, first_stack_number, second_stack_number = map(
        int, re.findall(r'\d+', movement_line))

    for i in range(n_items, 0, -1):
        item = stacks[first_stack_number-1].pop(-i)
        stacks[second_stack_number-1].append(item)


with open('./5/input.txt') as file:
    number_of_stacks = 1
    line = file.readline().replace('\n', '')
    stack_lines = []

    while line[1] != '1':
        stack_lines.append(line)
        number_of_stacks += 1
        line = file.readline().replace('\n', '')

    stacks = build_stacks(stack_lines)

    movement_lines = file.read().strip().split('\n')
    for movement_line in movement_lines:
        move_items(stacks, movement_line)

    top_items = map(lambda stack: stack.pop(), stacks)
    print(''.join(top_items))
