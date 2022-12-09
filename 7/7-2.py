class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.subdirs = []


def find_dir_size(dir: Dir, terminal_lines: 'list[str]', line_position: int) -> int:
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

            position_where_subcall_stopped = find_dir_size(
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


def find_dirs_sizes_gte_N(dir: Dir, size_list: 'list[int]', N: int):
    if dir.size >= N:
        size_list.append(dir.size)

    for subdir in dir.subdirs:
        find_dirs_sizes_gte_N(subdir, size_list, N)

    return size_list


with open('./7/input.txt') as file:
    terminal_lines = file.read().strip().split('\n')
    root = Dir('/')
    find_dir_size(root, terminal_lines, 1)
    
    disk_total_space = 70000000
    used_space = root.size
    unused_space = disk_total_space - used_space
    required_unused_space = 30000000
    minimum_space_to_free = required_unused_space - unused_space

    candidates = find_dirs_sizes_gte_N(root, [], minimum_space_to_free)
    print(min(candidates))
