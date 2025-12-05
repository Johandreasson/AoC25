
with open("5/inp.txt") as f:
    inp = f.read().splitlines()

inp1 = ["..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."]

def check_adjacent(i, j):
    rolls = 0
    for l in range(i-1, i+2):
        if l < 0 or l > len(inp):
            continue
        for m in range(j-1, j+2):
            if m < 0 or m > len(inp[0]):
                continue
            try:
                if inp[l][m] == "@":
                    rolls += 1
            except IndexError:
                continue
    if rolls < 5:
        return True
accessible_rolls = 0
while True:
    
    for i, row in enumerate(inp):
        new_row = ""
        for j, roll in enumerate(row):
            if roll == "@" and check_adjacent(i, j):
                print("x", end="")
                new_row += "."
                accessible_rolls += 1
            else:
                print(roll, end="")
                new_row += roll
        inp[i] = new_row
        print()

    print(accessible_rolls)