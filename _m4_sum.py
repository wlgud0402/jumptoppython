#총합// 50점 이상만
A = [20,55,67,82,45,33,90]

result =0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark

print(result)