with open('latex.log') as f:
    line = f.readlines()
    line = set(line)
    print('共{}关键行'.format(len(line)))