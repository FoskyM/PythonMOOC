str = input()
new_str = ""
for s in str:
    if 'a' <= s <= 'z':
        new_str += chr(ord('a') + ((ord(s) - ord('a')) + 3) % 26)
    elif 'A' <= s <= 'Z':
        new_str += chr(ord('A') + ((ord(s) - ord('A')) + 3) % 26)
    else:
        new_str += s
print(new_str)