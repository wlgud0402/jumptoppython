#정규포현실ㄹ

import re
p = re.compile('[a-z]+')

result = p.findall("life is too short")
print(result)


print()
print()


result2 = p.finditer("life is too short")
print(result2)

print()
for r in result2:
    print(r)