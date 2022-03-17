#input 사용법
#기본 타입은 str

#예제1

name = input("Enter your name")
grade = input("Enter your grade")
company = input("Enter your company")

print(name, grade, company)

# 예제2
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number", type(number))
print("type of name", type(name))
#기본타임이 str 이다

#예제3
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print('total : ', total)

