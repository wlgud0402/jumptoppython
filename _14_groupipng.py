#그루핑
import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

print()

print(m.group(0))