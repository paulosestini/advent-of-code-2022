def load_forest_matrix(filepath):
    with open(filepath) as file:
        file_content = file.read().strip()
        forest = map(list, file_content.split('\n'))
        forest = map(lambda row: list(map(int, row)), forest)
    return list(forest)


def cast_ray(ray_height, forest_row):
    intersected_positions = {}
    j = 0
    while j < len(forest_row):
        tree = forest_row[j]
        if tree >= ray_height:
            intersected_positions[j] = True
            break
        j += 1
    return intersected_positions


forest = load_forest_matrix('./8/input.txt')

visible_trees = {}

for row_index in range(len(forest)):
    for i in range(10):
        intersected_positions = cast_ray(i, forest[row_index])
        for pos in intersected_positions.keys():
            visible_trees[(row_index, pos)] = True

    for i in range(10):
        intersected_positions = cast_ray(i, forest[row_index][::-1])
        for pos in intersected_positions.keys():
            visible_trees[(row_index, len(forest[row_index]) - 1 - pos)] = True

for col_index in range(len(forest[0])):
    transposed_column = [forest[row_index][col_index]
                         for row_index in range(len(forest))]

    for i in range(10):
        intersected_positions = cast_ray(i, transposed_column)
        for pos in intersected_positions.keys():
            visible_trees[(pos, col_index)] = True

    for i in range(10):
        intersected_positions = cast_ray(i, transposed_column[::-1])
        for pos in intersected_positions.keys():
            visible_trees[(len(transposed_column) - 1 - pos, col_index)] = True

print(len(visible_trees.keys()))
