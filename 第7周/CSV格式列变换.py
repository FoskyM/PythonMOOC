with open('data.csv') as f:
    for line in f:
        line = line.strip("\n")
        ls = line.split(",")
        ls = ls[::-1]
        print(",".join(ls))
