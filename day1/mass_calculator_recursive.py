def calc_total_fuel( datum ):
    smol_datum = datum // 3 - 2
    if smol_datum <= 0:
        return 0
    #print(smol_datum)
    return smol_datum + calc_total_fuel( smol_datum )

data_path = './mass_data.txt'
mass_file = open(data_path, 'r')
mass_data = mass_file.read().splitlines()
total_fuel = 0

for datum in mass_data:
    total_fuel += calc_total_fuel(int(datum))

print(total_fuel)