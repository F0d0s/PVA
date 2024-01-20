import math

point1 = []

point2 = []

sidelength_input = input("Rozmer mistnosti: ")

is_on_wall_1 = False
is_on_wall_2 = False

if sidelength_input.isnumeric() == False or int(sidelength_input) == 0:
    print("Nespravny vstup.")
    exit()
else:
    sidelength = int(sidelength_input)

point_input1 = input("Bod #1: ")
point_input1 = point_input1.split()

for i in point_input1:
    if (i.isnumeric() == False) or (0 < int(i) < 20) or (sidelength - 20 < int(i) > sidelength):
        print("Nespravny vstup.")
        exit()
    if int(i) == 0 or int(i) == sidelength:
        is_on_wall_1 = True
    if len(point_input1) != 3:
        print("Nespravny vstup.")
        exit()
if is_on_wall_1 == False:
    print("Nespravny vstup.")
    exit()
point1 = [int(i) for i in point_input1]  

point_input2 = input("Bod #2: ")
point_input2 = point_input2.split()
for i in point_input2:
    if (i.isnumeric() == False) or (0 < int(i) < 20) or (sidelength - 20 < int(i) > sidelength):
        print("Nespravny vstup.")
        exit()
    if int(i) == 0 or int(i) == sidelength:
        is_on_wall_2 = True
    if len(point_input2) != 3:
        print("Nespravny vstup.")
        exit()
if is_on_wall_2 == False:
    print("Nespravny vstup.")
    exit()
point2 = [int(i) for i in point_input2]

def are_points_on_opposite_sides(point1, point2, sidelength):
    return (
        (point1[0] == 0 and point2[0] == sidelength) or
        (point2[0] == 0 and point1[0] == sidelength) or
        (point1[1] == 0 and point2[1] == sidelength) or
        (point2[1] == 0 and point1[1] == sidelength) or
        (point1[2] == 0 and point2[2] == sidelength) or
        (point2[2] == 0 and point1[2] == sidelength)
    )

def edge_distances (p, side):
    distances = [p[0], p[1], side - p[0], side - p[1]]
    return distances

def calculate_pipes (p1, p2, side):
    if are_points_on_opposite_sides(point1, point2, sidelength):
        p1 = [i for i in p1 if (i != 0 and i != side)]
        p2 = [i for i in p2 if (i != 0 and i != side)]
        distances1 = edge_distances(p1, side)
        distances2 = edge_distances(p2, side)
        distances = []
        for i in range(4):
            longer_pendant = distances1[i] + distances2[i] + side
            if i%2 == 0:
                shorter_pendant = abs(p1[1] - p2[1])
            else:
                shorter_pendant = abs(p1[0] - p2[0])
            distances.append(longer_pendant + shorter_pendant)
        distance = min(distances)
    else:
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
    return distance

def calculate_hoses (p1, p2, side):
    if are_points_on_opposite_sides(point1, point2, sidelength):
        p1 = [i for i in p1 if (i != 0 and i != side)]
        p2 = [i for i in p2 if (i != 0 and i != side)]
        distances1 = edge_distances(p1, side)
        distances2 = edge_distances(p2, side)
        distances = []
        for i in range(4):
            longer_pendant = distances1[i] + distances2[i] + side
            if i%2 == 0:
                shorter_pendant = abs(p1[1] - p2[1])
            else:
                shorter_pendant = abs(p1[0] - p2[0])
            distances.append(math.sqrt(longer_pendant**2 + shorter_pendant**2))
        distance = min(distances)
    else:
        for i in range(3):
            if p1[i] == 0 or p1[i] == side:
                axis1 = i
            if p2[i] == 0 or p2[i] == side:
                axis2 = i     
        other_axis = [i for i in range(3) if i != axis1 and i != axis2][0]   
        distance = math.sqrt((abs(p1[axis1] - p2[axis1]) + abs(p1[axis2] - p2[axis2]))**2 + abs(p1[other_axis] - p2[other_axis])**2)
    return distance

print(f"Delka trubek: {calculate_pipes(point1, point2, sidelength)}")
print(f"Delka hadice: {calculate_hoses(point1, point2, sidelength)}")
