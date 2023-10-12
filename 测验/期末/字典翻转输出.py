d = eval(input())
output = {}
try:

    for k in d:
        output[d[k]] = k
    print(output)

except:
    print("输入错误")