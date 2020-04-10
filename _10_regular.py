import re
p = re.compile('[a-z]+')

m = p.match("python")

print(m.group())
print(m.start())
print(m.end())
print(m.span())


print()
print()

n = p.search("3 python")
print(n.group())
print(n.start())
print(n.end())
print(n.span())