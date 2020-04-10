#숫자 총합 구하기
user_input = input("숫자를 입력하시요>")

numbers = user_input.split(",")
total = 0
for number in numbers:
    total += int(number)
print(total)


#입력하는 숫자의 형식: 15,22,94,48,26,48,15