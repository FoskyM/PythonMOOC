TempStr = input()
Str = TempStr.replace('1', "一").replace('2', "二").replace('3', "三").replace('4', "四").replace('5', "五").replace('6', "六").replace('7', "七").replace('8', "八").replace('9', "九").replace('0', "零")
print(Str)

# template = "零一二三四五六七八九"
#
# s = input()
# for c in s:
#     print(template[eval(c)], end="")