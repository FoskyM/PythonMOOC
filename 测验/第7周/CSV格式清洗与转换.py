with open('data.csv') as f:
    ls = []

    for line in f.readlines():
        line = line.strip("\n").replace(" ", "")
        data = ";".join(line.split(",")[::-1])
        ls.insert(0, data)

    for row in ls:
        print(row)
