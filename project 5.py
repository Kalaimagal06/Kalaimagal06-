import re

s="Hi Hello. I am kalai. This is my file"

pattern=r'\.'

match=re.sub(pattern,'_',s)

print(match)
