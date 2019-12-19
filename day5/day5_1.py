# Day 5 Part 1
# Read the data file
path = 'data.txt'
data_file = open(path, 'r')
data_file_str = data_file.read()
data_array = list(map(int, data_file_str.split(",")))

current_index = 0
index_increment = 0
while current_index < len(data_array):
    # print(current_index)
    # print(data_array)
    opcode = data_array[current_index]
    # This turns the opcode into a list of it's digits
    opcode_digit_list = [int(x) for x in str(opcode)]
    # print(opcode_digit_list)
    operation = 0
    # Fetch the operation alongside other pertinent info
    # 0 is address mode and 1 is immediate mode
    arg1_mode = arg2_mode = arg3_mode = 0
    for i, digit in enumerate(range(len(opcode_digit_list) - 1, -1, -1)):
        cur_val = opcode_digit_list[digit]
        if i == 0:
            operation += cur_val
        elif i == 1:
            operation += cur_val * 10
        elif i == 2:
            arg1_mode = cur_val
        elif i == 3:
            arg2_mode = cur_val
        elif i == 4:
            arg3_mode = cur_val

    # End if we see 99
    if operation == 99:
        break

    # Correctly set the argument values
    arg1 = data_array[current_index + 1]
    arg2 = data_array[current_index + 2]
    arg3 = data_array[current_index + 3]

    if operation == 1 or operation == 2 or operation == 4:
        if arg1_mode == 0 and arg1 < len(data_array):
            arg1 = data_array[arg1]
        if arg2_mode == 0 and arg2 < len(data_array):
            arg2 = data_array[arg2]

#    print("arg1 is " + str(arg1))
#    print("arg2 is " + str(arg2))
#    print("arg3 is " + str(arg3))

    if operation == 1:
        data_array[arg3] = arg1 + arg2
        index_increment = 4
    elif operation == 2:
        data_array[arg3] = arg1 * arg2
        index_increment = 4
    elif operation == 3:
        val = int(input('-->'))
        data_array[arg1] = val
        index_increment = 2
    elif operation == 4:
        print("OUTPUT IS " + str(arg1))
        index_increment = 2
    else:
        print("INVALID OPCODE " + str(operation))
        break
    # Increment the index based on the operation
    current_index += index_increment
print(data_array)
print(data_array[0])
