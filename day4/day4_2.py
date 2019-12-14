# My puzzle input is 382345-843167
total_valid = 0
for i in range(382345, 843168):
    val_list = [int(x) for x in str(i)]
    adjacent_val = False
    increasing_val = True
    num_adjacent = 1
    for num, i in enumerate(val_list):
        if num == 0:
            continue
        if val_list[num] == val_list[num - 1]:
            num_adjacent += 1
            if (num == len(val_list) - 1) and num_adjacent == 2:
                adjacent_val = True
        elif num_adjacent == 2:
            adjacent_val = True
            num_adjacent = 1
        else:
            num_adjacent = 1
        if val_list[num] < val_list[num - 1]:
            increasing_val = False
    if adjacent_val and increasing_val:
        total_valid += 1

print(total_valid)
