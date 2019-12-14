data_path = './mass_data.txt'
mass_file = open(data_path, 'r')
mass_data = mass_file.read().splitlines()

total_fuel = 0
for datum in mass_data:
    total_fuel += (int(datum) // 3) - 2

print(total_fuel)