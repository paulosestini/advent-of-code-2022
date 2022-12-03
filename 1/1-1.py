with open('./1/input.txt') as file:
    file_content = file.read().strip()
    elves_calories_raw_text_list = file_content.split('\n\n')
    elves_calories_lists = map(
        lambda elf_calories_raw_text: elf_calories_raw_text.split('\n'),
        elves_calories_raw_text_list)
    elves_total_calories = map(
        lambda calorie_list: sum(map(lambda x: int(x), calorie_list)),
        elves_calories_lists
    )
    print(max(elves_total_calories))
