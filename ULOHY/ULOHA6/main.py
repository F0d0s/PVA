import sys

def load_data():
    try:
        lines = sys.stdin.read().strip().split("\n")
        if not lines:
            raise ValueError
        
        shelves = {}
        i = 0
        
        while i < len(lines) and lines[i].strip():
            line = lines[i].strip()
            if line.startswith("#"):
                shelf_id = int(line[1:])
                if shelf_id != len(shelves):
                    raise ValueError
                shelves[shelf_id] = []
                i += 1
                while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                    shelves[shelf_id].append(lines[i].strip())
                    i += 1
            else:
                raise ValueError
        
        if i == len(lines) or lines[i].strip():
            raise ValueError
        
        i += 1
        shopping_lists = []
        current_list = []
        
        while i < len(lines):
            if lines[i].strip():
                current_list.append(lines[i].strip())
            else:
                if current_list:
                    shopping_lists.append(current_list)
                    current_list = []
            i += 1
        if current_list:
            shopping_lists.append(current_list)
        
        return shelves, shopping_lists
    except:
        print("Nespravny vstup.")
        sys.exit(1)

def find_item_in_shelves(shelves, item):
    for shelf_id, items in shelves.items():
        for shelf_item in items:
            if item.lower() == shelf_item.lower():
                return (shelf_id, shelf_item)
    for shelf_id, items in shelves.items():
        for shelf_item in items:
            if item.lower() in shelf_item.lower():
                return (shelf_id, shelf_item)
    return None

def optimize_shopping_list(shelves, shopping_list):
    found_items = []
    not_found_items = []
    
    for item in shopping_list:
        found_item = find_item_in_shelves(shelves, item)
        if found_item:
            found_items.append((item, *found_item))
        else:
            not_found_items.append((item, "N/A", ""))
    
    found_items.sort(key=lambda x: (x[1], shopping_list.index(x[0])))
    
    optimized_list = found_items + not_found_items
    return optimized_list

def main():
    shelves, shopping_lists = load_data()
    
    for shopping_list in shopping_lists:
        print("Optimalizovany seznam:")
        optimized_list = optimize_shopping_list(shelves, shopping_list)
        for idx, (item, shelf_id, shelf_item) in enumerate(optimized_list):
            if shelf_id == "N/A":
                print(f" {idx}. {item} -> {shelf_id}")
            else:
                print(f" {idx}. {item} -> #{shelf_id} {shelf_item}")
        print()

main()

## Input do terminalu a ctrl+z -> enter
