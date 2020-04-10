#곱하기

user_input = input("구구단을 출력할 숫자를 입력하세요>")

num = int(user_input)
for i in range(1, 10):
    print(i*num, end= ' ')