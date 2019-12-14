# My puzzle input is 382345-843167
#i = 112233
i = 123444
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
            print("setting adj value true at " + str(num) + " " + str(i))
            adjacent_val = True
    elif num_adjacent == 2:
        print("2 setting adj value true at " + str(num) + " " + str(i))
        adjacent_val = True
        num_adjacent = 1
    else:
        num_adjacent = 1
    if val_list[num] < val_list[num - 1]:
        increasing_val = False

print(adjacent_val and increasing_val)
