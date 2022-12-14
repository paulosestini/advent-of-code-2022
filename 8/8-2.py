def load_forest_matrix(filepath):
    with open(filepath) as file:
        file_content = file.read().strip()
        forest = map(list, file_content.split('\n'))
        forest = map(lambda row: list(map(int, row)), forest)
    return list(forest)


def cast_ray(ray_height, forest_row):
    j = 0
    while j < len(forest_row):
        tree = forest_row[j]
        if tree >= ray_height:
            return j + 1
        j += 1

    return j


def calculate_scenic_score(row_index, col_index, forest):
    left_trees = forest[row_index][:col_index]
    right_trees = forest[row_index][col_index +1:]
    top_trees = [forest[i][col_index] for i in range(row_index)]
    down_trees = [forest[i][col_index] for i in range(row_index+1, len(forest))]

    left_distance = cast_ray(forest[row_index][col_index], left_trees[::-1])
    right_distance = cast_ray(forest[row_index][col_index], right_trees)
    top_distance = cast_ray(forest[row_index][col_index], top_trees[::-1])
    down_distance = cast_ray(forest[row_index][col_index], down_trees)

    return left_distance * right_distance * top_distance * down_distance


forest = load_forest_matrix('./8/input.txt')

max_scenic_score = 0

for row_index in range(len(forest)):
    for col_index in range(len(forest[0])):
        score = calculate_scenic_score(row_index, col_index, forest)
        max_scenic_score = score if score > max_scenic_score else max_scenic_score

print(max_scenic_score)
