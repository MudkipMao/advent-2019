path = 'data.txt'
data_file = open(path, 'r')

data_file_str = data_file.read()

target = 19690720

for i in range(100):
    for j in range(100):
        data_array = list(map(int, data_file_str.split(",")))

        data_array[1] = i
        data_array[2] = j

        current_index = 0
        while current_index < len(data_array):
            opcode = data_array[current_index]
            if opcode == 99:
                break
            val = 0
            arg1 = data_array[current_index + 1]
            arg2 = data_array[current_index + 2]
            if opcode == 1:
                val = data_array[arg1] + data_array[arg2]
            if opcode == 2:
                val = data_array[arg1] * data_array[arg2]
            data_array[data_array[current_index + 3]] = val
            current_index += 4
        if data_array[0] == target:
            print(100 * i + j)
            print(data_array[0])
