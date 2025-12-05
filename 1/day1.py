with open("1/inp.txt") as f:
    inp = f.read().splitlines()

dial = 50
pw = 0

for rotation in inp:
    direction = rotation[0]
    for times in range(int(rotation[1:])):
        if direction == "L":
            dial -= 1
        else:
            dial += 1
        if dial > 99:
            dial = 0
        if dial < 0:
            dial = 99
        if dial == 0:
            pw += 1
print(pw)