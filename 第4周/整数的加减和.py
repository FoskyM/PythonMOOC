k = 1
sum = 0
for i in range(966):
    sum += (i + 1) * k
    k = -k

print(sum)

# s = 0
# count = 1
# while count <=966:
#     if count%2 == 0:
#         s -= count
#     else:
#         s += count
#     count += 1
# print(s)