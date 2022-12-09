class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.subdirs = []


def calculate_dir_size(dir: Dir, terminal_lines: 'list[str]', line_position: int) -> int:
    while line_position < len(terminal_lines):
        line = terminal_lines[line_position]
        tokens = line.split(' ')

        should_change_directory = (tokens[0] == '$' and tokens[1] == 'cd')
        if should_change_directory:
            dirname = tokens[2]
            should_return = (dirname == '..')

            if (should_return):
                sum_of_subdirs_sizes = sum(
                    map(lambda dir: dir.size, dir.subdirs))
                dir.size += sum_of_subdirs_sizes
                return line_position

            subdir_to_change_to = list(filter(lambda subdir: subdir.name ==
                                              dirname, dir.subdirs))[0]

            position_where_subcall_stopped = calculate_dir_size(
                subdir_to_change_to, terminal_lines, line_position+1)
            line_position = position_where_subcall_stopped

        elif tokens[0] != '$':
            if tokens[0] == 'dir':
                dir.subdirs.append(Dir(tokens[1]))
            else:
                dir.size += int(tokens[0])

        line_position += 1

    sum_of_subdirs_sizes = sum(
        map(lambda dir: dir.size, dir.subdirs))
    dir.size += sum_of_subdirs_sizes
    
    return line_position


def find_dirs_sizes_lt_N(dir: Dir, size_list: 'list[int]', N: int):
    if dir.size <= N:
        size_list.append(dir.size)

    for subdir in dir.subdirs:
        find_dirs_sizes_lt_N(subdir, size_list, N)

    return size_list


with open('./7/input.txt') as file:
    terminal_lines = file.read().strip().split('\n')
    root = Dir('/')
    calculate_dir_size(root, terminal_lines, 1)
    sizes = find_dirs_sizes_lt_N(root, [], 100000)
    print(sum(sizes))
