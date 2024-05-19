import sys
import math

def parse_input_line(line):
    try:
        coords, name = line.split(':')
        x, y = map(float, coords.split(','))
        name = name.strip()
        if not name or len(name) > 199:
            raise ValueError
        return (x, y, name)
    except:
        raise ValueError("Nespravny vstup.")

def calculate_distance(plane1, plane2):
    return math.sqrt((plane1[0] - plane2[0])**2 + (plane1[1] - plane2[1])**2)

def main():
    print("Pozice letadel:")
    
    planes = []

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            planes.append(parse_input_line(line))
    except ValueError as e:
        print(e)
        return
    
    if len(planes) < 2:
        print("Nespravny vstup.")
        return
    
    min_distance = float('inf')
    closest_pairs = []
    
    for i in range(len(planes)):
        for j in range(i + 1, len(planes)):
            dist = calculate_distance(planes[i], planes[j])
            if dist < min_distance:
                min_distance = dist
                closest_pairs = [(planes[i][2], planes[j][2])]
            elif dist == min_distance:
                closest_pairs.append((planes[i][2], planes[j][2]))
    
    print(f"Vzdalenost nejblizsich letadel: {min_distance:.6f}")
    print(f"Nalezenych dvojic: {len(closest_pairs)}")
    for pair in closest_pairs:
        print(f"{pair[0]} - {pair[1]}")

main()

## Input do terminalu a ctrl+z -> enter
