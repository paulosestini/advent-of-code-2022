from functools import reduce


def get_item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 1 + 26


def get_compartment_bitmap(compartment: str) -> int:
    return reduce(lambda bitmap, item: bitmap | 1 << get_item_priority(item), compartment, 0)


def get_rucksack_bitmap_intersection(rucksack: str) -> int:
    middle = len(rucksack) // 2 - 1
    compartment1, compartment2 = rucksack[:middle+1], rucksack[middle+1:]
    bitmap1, bitmap2 = get_compartment_bitmap(
        compartment1), get_compartment_bitmap(compartment2)
    return bitmap1 & bitmap2


def get_priority_from_bitmap(bitmap: int) -> int:
    priority = 0
    while (1 << priority) != bitmap:
        priority += 1
    return priority


rucksacks = None
with open('./3/input.txt') as file:
    rucksacks = map(lambda line: line.strip(), file.readlines())
    rucksacks_bitmap_intersections = map(
        get_rucksack_bitmap_intersection, rucksacks)
    rucksacks_repeated_priorities = map(
        get_priority_from_bitmap, rucksacks_bitmap_intersections)
    print(sum(rucksacks_repeated_priorities))
