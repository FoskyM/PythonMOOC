f = open('latex.log')
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)

r = set(ls)
print("共{}独特行".format(len(s) - len(r)))
