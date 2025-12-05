
with open("2/inp.txt") as f:
    inp = f.read().split(",")

invalid = 0
for seq in inp:
    seq = seq.split("-")
    for id in range(int(seq[0]), int(seq[1])+1):
        id = str(id)
        half = int(len(id)/2)
        for i in range(half+1):
            duplicates = []
            try:
                duplicates = id.split(id[:i])
                if len(duplicates) > 2 and all(x == "" for x in duplicates):
                    invalid += int(id)
                    break
            except ValueError:
                pass

print(invalid)