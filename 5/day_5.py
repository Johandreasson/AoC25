
with open("5/inp.txt") as f:
    inp = f.read().splitlines()

test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
test = test.splitlines()

ranges = []
ingredients = []
is_range = True
for item in inp:
    if item == "":
        is_range = False
        continue
    if is_range:
        int_range = [int(item.split("-")[0]), int(item.split("-")[1])]
        ranges.append(int_range)
    else:
        ingredients.append(item)


fresh = 0
for ingredient in ingredients:
    for fresh_range in ranges:
        if int(ingredient) in range(fresh_range[0], fresh_range[1]+1):
            fresh += 1
            break
print(fresh)