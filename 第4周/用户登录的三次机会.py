user = 'Kate'
pswd = '666666'

for i in range(3):
    u = input()
    p = input()

    if (u == user and p == pswd):
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")


# count = 0
# while count < 3:
#     name = input()
#     password = input()
#     if name == 'Kate'and password == '666666':
#         print("登录成功！")
#         break
#     else:
#         count += 1
#         if count == 3:
#             print("3次用户名或者密码均有误！退出程序。")