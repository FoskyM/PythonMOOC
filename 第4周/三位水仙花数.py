from math import pow

s = ""

for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i % 10

    if (pow(a, 3) + pow(b, 3) + pow(c, 3)) == i:
        s += "{},".format(i)

print(s[:-1])

# s = ""
# for i in range(100, 1000):
#     t = str(i)
#     if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
#         s += "{},".format(i)
# print(s[:-1])