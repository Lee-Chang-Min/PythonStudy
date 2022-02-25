#데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0
int_v = 7
list = [str1, str2]
    
print(list) 

dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}   
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
""" + - / * 
//:몫만 계산
%: 나머지만 계산 
abs(x): 절대값
pow(x,y) x ** y - > 2^3 x의 y제곱
"""

#정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777755555555555555
print(big_int)

#실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

#연산 실습
i1 = 39
i2 = 939
big_int1 = 79999999999999999954632132154654
big_int2 = 3421654654864354111111111111111111
f1 = 1.23454654
f2 = 3.9321654

print(">>>>>>>+")

#형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

#타입 출력
print(type(a),  type(b), type(c), type(d))
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # true : 1, false : 0
print(float(False))
print(complex(3))
print(complex('3')) #문자형 -> 숫자형
print(complex(False))

#수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5**3)

#외부모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)

