
def parte_1():
    with open("input_day01.txt", "r") as data:
        left_data, right_data = zip(*[(int(line.split()[0]), int(line.split()[-1])) for line in data])

    left_data = sorted(left_data)
    right_data = sorted(right_data)

    distances = [abs(ld - rd) for ld, rd in zip(left_data, right_data)]

    print(sum(distances))
    
def parte_2():
    with open("input_day01.txt", "r") as data:
        left_data, right_data = zip(*[(int(line.split()[0]), int(line.split()[-1])) for line in data])
    
    similarities = []
    
    for item in left_data:
        similarities.append(item * right_data.count(item))
    
    print(sum(similarities))
        

def main():
    parte_1()
    parte_2()
    
if __name__ == "__main__":
    main()