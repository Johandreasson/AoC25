
with open("3/inp.txt") as f:
    inp = f.read().splitlines()

def part1():
    joltage = 0
    for bank in inp:
        most = 0
        for i, battery in enumerate(bank):
            try:
                for j in range(i+1, len(bank)):
                    if int(battery + bank[j]) > most:
                        most = int(battery + bank[j]) 
            except IndexError:
                break
        joltage += most

    print(joltage)

def part2():
    joltage = 0
    for bank in inp:
        n = 12
        most_total = ""
        index = 0
        for i in range(n, 0, -1):
            most = 0
            temp_index = 0
            for j in range(index, len(bank)+1):
                if i+j == len(bank)+1:
                    break
                if int(bank[j]) > most:
                    most = int(bank[j])
                    temp_index = j
            most_total += str(most)
            index = temp_index+1
            
        joltage += int(most_total)
    print(joltage)

part1()
part2()