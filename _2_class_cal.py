#사칙연산

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
        
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
b = FourCal(3,8)

print(a.add())
print(b.mul())


print()
#클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreFourCal(4,2)
print(c.add())

d = MoreFourCal(3,4)
print(d.pow())

print()
#나누는 값이 0일때 0을 돌려줘보자
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

e = SafeFourCal(4,0)
print(e.div())