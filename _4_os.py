import os

print(os.environ)

print()
print()

print(os.getcwd())

print()
print()

print(os.system("dir"))

print()
print()

f = os.popen("dir")
print(f.read())

print()
print()

