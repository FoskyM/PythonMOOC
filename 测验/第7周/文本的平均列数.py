f = open('latex.log')
row_count = 0
char_count = []
for line in f:
    line = line.strip('\n')
    if line == '':
        continue
    char_count.append(len(line))
    row_count += 1
f.close()
print(round(sum(char_count) / row_count))
