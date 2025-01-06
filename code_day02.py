def is_asc(data):
    return all(i < j for i, j in data)

def is_desc(data):
    return all( i > j for i, j in data)

def calc_subs(data):
    return [i - j for i, j in data]

def eval_subs(data):
    count = 0
    for item in data:
        if not 1 <= abs(item) <= 3:
            count = count + 1
            
    return count
    # return all( ( abs(diff) >= 1 and abs(diff) <= 3 ) for diff in data)

def analize_data_parte1(data):
    
    data_tuplas = list(zip(data, data[1:]))
    
    asc = is_asc(data_tuplas)
    desc = is_desc(data_tuplas)
    
    if not asc and not desc:
        return False
    
    subs = calc_subs(data_tuplas)
    subs_result = eval_subs(subs)
    diffs_ok = subs_result == 0
        
    return True if diffs_ok else False

def analize_data_parte2(data):
    tmp = []
    tmp_parte_1 = False
    for i in range(len(data) + 1):
        tmp = data[:i] + data[i+1:]
        tmp_parte_1 = analize_data_parte1(tmp)
        
        if tmp_parte_1:
            return tmp_parte_1
    
    if not tmp_parte_1:
        return tmp_parte_1
    

def analize_data(process_part_2 = False):
    data = []
    reports_parte1 = []
    reports_parte2 = []

    with open("input_day02.txt", "r") as file:
        for line in file:
            data = list(map(int,line.split()))
            
            parte_1 = analize_data_parte1(data)
            
            if parte_1:
                reports_parte1.append('SAFE')
            else:
                if not process_part_2:
                    reports_parte1.append('UNSAFE')
                else:
                    parte_2 = analize_data_parte2(data)
                    reports_parte2.append('SAFE') if parte_2 else reports_parte2.append('UNSAFE')
    
    total_part_1 = reports_parte1.count('SAFE')
    total_part_2 = reports_parte2.count('SAFE')
    
    print(f"Total safe reports part 1: {total_part_1}")
    if (process_part_2):
        print(f"Total safe reports part 2: {total_part_1 + total_part_2}")

def main():
    analize_data(True)
    

if __name__ == "__main__":
    main()