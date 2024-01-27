import math
        
point1 = []
point2 = []
point3 = []

point1_input = input("Bod A: ").split()

for i in range(len(point1_input)):
    p = point1_input[i]
    try:
        float(p)
        isnumber = True
    except ValueError:
        isnumber = False
    if isnumber == False:
        print("Nespravny vstup.")
        exit()
    
if len(point1_input) != 2:
    print("Nespravny vstup.")
    exit()
        
point1 = [float(i) for i in point1_input]
        
point2_input = input("Bod B: ").split()

for i in range(len(point2_input)):
    p = point2_input[i]
    try:
        float(p)
        isnumber = True
    except ValueError:
        isnumber = False
    if isnumber == False:
        print("Nespravny vstup.")
        exit()
        
if len(point2_input) != 2:
    print("Nespravny vstup.")
    exit()
        
point2 = [float(i) for i in point2_input]       

point3_input = input("Bod C: ").split()

for i in range(len(point3_input)):
    p = point3_input[i]
    try:
        float(p)
        isnumber = True
    except ValueError:
        isnumber = False
    if isnumber == False:
        print("Nespravny vstup.")
        exit()
        
if len(point3_input) != 2:
        print("Nespravny vstup.")
        exit()
        
point3 = [float(i) for i in point3_input]

if point1 == point2 == point3 or (point1 == point2 or point1 == point3 or point2 == point3):
    print("Nektere body splyvaji.")
    exit()

def are_points_collinear(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) - p1[1] * (p2[0] - p3[0]) + (p2[0] * p3[1]) - (p3[0] * p2[1]) == 0

def find_middle_point(p1, p2, p3):
    if (p1[0] <= p2[0] <= p3[0] or p3[0] <= p2[0] <= p1[0]) and (p1[1] <= p2[1] <= p3[1] or p3[1] <= p2[1] <= p1[1]):
        return "B"
    elif (p2[0] <= p1[0] <= p3[0] or p3[0] <= p1[0] <= p2[0]) and (p2[1] <= p1[1] <= p3[1] or p3[1] <= p1[1] <= p2[1]):
        return "A"
    else:
        return "C"
    
if are_points_collinear(point1, point2, point3):
    print("Body lezi na jedne primce.")
    print(f"Prostredni je bod {find_middle_point(point1, point2, point3)}.")
else:    
    print("Body nelezi na jedne primce.")
