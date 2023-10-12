# 请在...补充一行或多行代码

def cmul(*n):
    sum = 1
    for item in n:
        sum *= item
    return sum
print(eval("cmul({})".format(input())))

# def cmul(a, *b):
#     m = a
#     for i in b:
#         m *= i
#     return m
#
# print(eval("cmul({})".format(input())))