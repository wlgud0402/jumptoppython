#그루핑된 문자열에 이름 붙이기

import re

p= re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d)")
m = p.search("park 010-6805-0402")

print(m.group("name"))