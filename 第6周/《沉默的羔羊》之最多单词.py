import jieba

txt = open("沉默的羔羊.txt", "r", encoding='utf-8').read()
ls = jieba.lcut(txt)
counts = {}
for word in ls:
    if len(word) >= 2:
        counts[word] = counts.get(word, 0) + 1

maxc = 0
maxw = ""
for k in counts:
    if counts[k] > maxc:
        maxc = counts[k]
        maxw = k
    elif counts[k] == maxc and k > maxw:
        maxw = k
print(maxw)