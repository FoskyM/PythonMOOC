num = eval(input())
for i in range(1, num + 1, 2):
    print("{0:^{1}}".format("*" * i, num))