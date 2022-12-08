def check_overlap(interval_a: str, interval_b: str) -> bool:
    a_min, a_max = interval_a.split('-')
    b_min, b_max = interval_b.split('-')
    a_min, a_max = int(a_min), int(a_max)
    b_min, b_max = int(b_min), int(b_max)

    a_contains_b_min = b_min >= a_min and b_min <= a_max
    b_contains_a_min = a_min >= b_min and a_min <= b_max

    return a_contains_b_min or b_contains_a_min


with open('./4/input.txt') as file:
    pair_lines = file.read().strip().split('\n')
    pairs = map(lambda pair_line: pair_line.split(','), pair_lines)
    fully_contains_amount = sum(map(lambda pair: check_overlap(*pair), pairs))
    print(fully_contains_amount)
