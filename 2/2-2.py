who_beats_map = {'A': 'B', 'B': 'C', 'C': 'A'}
who_loses_map = {'B': 'A', 'C': 'B', 'A': 'C'}
object_to_choose_map = {
    ('A', 'X'): who_loses_map['A'],
    ('A', 'Y'): 'A',
    ('A', 'Z'): who_beats_map['A'],
    ('B', 'X'): who_loses_map['B'],
    ('B', 'Y'): 'B',
    ('B', 'Z'): who_beats_map['B'],
    ('C', 'X'): who_loses_map['C'],
    ('C', 'Y'): 'C',
    ('C', 'Z'): who_beats_map['C']
}

object_points_map = {'A': 1, 'B': 2, 'C': 3}
match_points_map = {'Z': 6, 'Y': 3, 'X': 0}


def get_match_total_points(other_object, game_outcome):
    your_object = object_to_choose_map[(other_object, game_outcome)]
    total_points = object_points_map[your_object] + match_points_map[game_outcome]
    return total_points


with open('./2/input.txt') as file:
    game_total_points = sum(map(lambda match: get_match_total_points(
        *match.split(' ')), file.read().strip().split('\n')))
    print(game_total_points)
