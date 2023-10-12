s = input()
n = eval(s)
try:
    if complex(s) == complex(n):
        print(n ** 2)
except:
    print("输入有误")
