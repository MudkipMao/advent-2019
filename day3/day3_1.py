class line_data:
    def __init__(self):
        self.x_start = 0
        self.y_start = 0
        self.x_end = 0
        self.y_end = 0
        self.dire = 0 # 0 for horizontal, 1 for vertical
    def __str__(self):
        return "x_end: " + str(self.x_end) + ", y_end: " + str(self.y_end) + ", direction: " + str(self.dire)

data_file = open('data.txt', 'r')
#data_file = open('test_data1.txt', 'r')
#data_file = open('test_data2.txt', 'r')

first_line_raw = data_file.readline()
second_line_raw = data_file.readline()

first_line_list = first_line_raw.rstrip().split(',')
second_line_list = second_line_raw.rstrip().split(',')

first_line_coords = []
second_line_coords = []

curr_x = 0
curr_y = 0
for datum in first_line_list:
    curline = line_data()
    curline.x_start = curr_x
    curline.y_start = curr_y
    curline.x_end = curr_x
    curline.y_end = curr_y
    direction = datum[0]
    distance = datum[1:]
    if (direction == 'U'):
        curline.y_end += int(distance)
        curr_y += int(distance)
        curline.dire = 1
    if (direction == 'D'):
        curline.y_end -= int(distance)
        curr_y -= int(distance)
        curline.dire = 1
    if (direction == 'L'):
        curline.x_end -= int(distance)
        curr_x -= int(distance)
    if (direction == 'R'):
        curline.x_end += int(distance)
        curr_x += int(distance)
    #print(curline)
    first_line_coords.append(curline)

curr_x = 0
curr_y = 0
for datum in second_line_list:
    curline = line_data()
    curline.x_start = curr_x
    curline.y_start = curr_y
    curline.x_end = curr_x
    curline.y_end = curr_y
    direction = datum[0]
    distance = datum[1:]
    if (direction == 'U'):
        curline.y_end += int(distance)
        curr_y += int(distance)
        curline.dire = 1
    if (direction == 'D'):
        curline.y_end -= int(distance)
        curr_y -= int(distance)
        curline.dire = 1
    if (direction == 'L'):
        curline.x_end -= int(distance)
        curr_x -= int(distance)
    if (direction == 'R'):
        curline.x_end += int(distance)
        curr_x += int(distance)
    #print(curline)
    second_line_coords.append(curline)

smallest = float('inf')

for i in first_line_coords:
    for j in second_line_coords:
        if (i.dire == 0) and (j.dire == 1): # If line one is horizontal and line two is vertical
            if (i.x_start <= j.x_start <= i.x_end) or (i.x_end <= j.x_start <= i.x_start):
                if (j.y_start <= i.y_start <= j.y_end) or (j.y_end <= i.y_start <= j.y_start):
                    dist_val1 = abs(j.x_start) + abs(i.y_start)
                    print(str(dist_val1))
#            if j.x_start in range(*sorted((i.x_start,i.x_end))):
#                if i.y_start in range(*sorted((j.y_start,j.y_end))):
#                    dist_val1 = abs(j.x_start) + abs(i.y_start)
#                    print(str(dist_val1))
        if (i.dire == 1) and (j.dire == 0): # If line one is vertical and line two is horizontal
            if (j.x_start <= i.x_start <= j.x_end) or (j.x_end <= i.x_start <= j.x_start):
                if (i.y_start <= j.y_start <= i.y_end) or (i.y_end <= j.y_start <= i.y_start):
                    dist_val2 = abs(i.x_start) + abs(j.y_start)
                    print(str(dist_val2))
            #if i.x_start in range(*sorted((j.x_start,j.x_end))):
            #    if j.y_start in range(*sorted((i.y_start,i.y_end))):
            #        dist_val2 = abs(i.x_start) + abs(j.y_start)
            #        print(str(dist_val2))
        
