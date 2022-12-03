from functools import reduce


def get_item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 1 + 26


def get_rucksack_bitmap(compartment: str) -> int:
    return reduce(lambda bitmap, item: bitmap | 1 << get_item_priority(item), compartment, 0)


def get_group_intersection_bitmap(group: 'list[str]') -> int:
    group_bitmaps = list(map(get_rucksack_bitmap, group))
    return reduce(lambda result, bitmap: result & bitmap, group_bitmaps[1:], group_bitmaps[0])


def get_priority_from_bitmap(bitmap: int) -> int:
    priority = 0
    while (1 << priority) != bitmap:
        priority += 1
    return priority


rucksacks = None
with open('./3/input.txt') as file:
    rucksacks = list(map(lambda line: line.strip(), file.readlines()))
    grouped_rucksacks = map(lambda i: rucksacks[i: i+3], range(0, len(rucksacks), 3))
    group_intersection_bitmaps = map(get_group_intersection_bitmap, grouped_rucksacks)
    group_badge_priorities = map(get_priority_from_bitmap, group_intersection_bitmaps)
    print(sum(group_badge_priorities))