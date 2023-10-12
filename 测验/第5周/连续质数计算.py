# 请在...补充一行或多行代码

def prime(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n = int(n) + 1 if n > int(n) else int(n)
s = ""
count = 0
while count < 5:
    if prime(n):
        s += str(n) + ","
        count += 1
    n += 1

print(s[:-1])