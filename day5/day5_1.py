path = 'data.txt'
data_file = open(path, 'r')

data_file_str = data_file.read()
data_array = list(map(int, data_file_str.split(",")))
data_array[1] = 12
data_array[2] = 2

current_index = 0
while current_index < len(data_array):
    opcode = data_array[current_index]
    print(opcode)
    if opcode == 99:
        break
    val = 0
    if opcode == 1:
        val = data_array[data_array[current_index + 1]] + data_array[data_array[current_index + 2]]
    if opcode == 2:
        val = data_array[data_array[current_index + 1]] * data_array[data_array[current_index + 2]]
    data_array[data_array[current_index + 3]] = val
    current_index += 4
print(data_array)
print(data_array[0])
