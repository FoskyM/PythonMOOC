f = open("data.csv")
s = f.read()
s = s.replace(" ","")
print(s)
f.close()