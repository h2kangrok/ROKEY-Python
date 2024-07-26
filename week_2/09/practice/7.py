# MARK: 문제 7

with open("data.txt") as f:
    for line in f:
        print(line.strip())
f.close()
