token_map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
who_beats_map = {'A': 'B', 'B': 'C', 'C': 'A'}
object_points_map = {'A': 1, 'B': 2, 'C': 3}
match_points_map = {'win': 6, 'draw': 3, 'lost': 0}


def get_match_total_points(other_object, your_object):
    your_object = token_map[your_object]
    total_points = object_points_map[your_object]
    if (who_beats_map[other_object] == your_object):
        total_points += match_points_map['win']
    elif (other_object == your_object):
        total_points += match_points_map['draw']
    else:
        total_points += match_points_map['lost']
    return total_points


with open('./2/input.txt') as file:
    game_total_points = sum(map(lambda match: get_match_total_points(
        *match.split(' ')), file.read().strip().split('\n')))
    print(game_total_points)
