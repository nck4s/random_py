found = False
word = input()
s = input()
for x in word:
    if s == x:
        found = True
        break #exit the loop after finding the first match

if found:
    print('Found')