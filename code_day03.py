import re

def is_do(subdata):
    return subdata == "do()"

def is_dont(subdata):
    return subdata == "don't()"

def is_mul(subdata):
    return subdata.startswith("mul")

def get_numbers(subdata):
    
    regex_extract_numbers = r"\d+,\d+"
    match_subgroup = re.search(regex_extract_numbers, subdata)
            
    if match_subgroup:
        values = match_subgroup.group().split(",")
        
    return (values[0], values[1])

def calc_parte_1(data):
    total_mul = 0
    
    regex_part1 = r"mul\(\d{1,3},\d{1,3}\)"
    
    matches = re.findall(regex_part1, data)
    
    if matches:
        
        for match in matches:
            values = get_numbers(match) 
            total_mul += int(values[0]) * int(values[1])
            
    return total_mul

def calc_parte_2(data):
    is_enabled = True
    total_mul = 0
    regex_part2 = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    
    matches = re.findall(regex_part2, data)
    
    if matches:
        for match in matches:
            if is_do(match):
                is_enabled=True
            elif is_dont(match):
                is_enabled=False
            elif is_mul(match) and is_enabled:
                values = get_numbers(match) 
                total_mul += int(values[0]) * int(values[1])
                
    return total_mul
        
def main():
    with open("input_day03.txt", "r") as file:
        data = file.read()
        
    calc_parte1 = calc_parte_1(data)
    calc_parte2 = calc_parte_2(data)
               
    print("Total mul parte 1: ", calc_parte1)
    print("Total mul parte 2: ", calc_parte2)
    
    
if __name__ == "__main__":
    main()