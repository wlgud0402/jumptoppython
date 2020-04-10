class calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):         #더하기기능
        self.result += num
        return self.result

    def sub(self, num):         #빼기기능
        self.result -= num
        return self.result

cal1 = calculator()
cal2 = calculator()

print(cal1.add(3))
print(cal1.add(4))

print()

print(cal2.add(3))
print(cal2.add(7))