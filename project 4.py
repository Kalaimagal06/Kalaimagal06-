import re
s="Hi Hello, this is my file"
pattern = r'\s+'
match = re.split(pattern, s)
print (match)
for i in match:
    print (i)