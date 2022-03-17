# 파이썬 반복문
# FOR 실습

# 코딩의 핵심 
# for i in <collection>
#     <loop body>

for v1 in range(10): #0~9
    print('v1 is : ', v1)
    
print()    
for v2 in range(1, 11):
    print('v2 is : ', v2)

print()   
for v3 in range(1, 11, 2):
    print('v3 is : ', v3)
    
#1~1000합

sum1 = 0

for v in range(1, 101):
    sum1 += v #sum1 = sum1 + v
    print('1~1000 Sum: ', sum1)
    
    print('1~1000 Sum : ', sum(range(1, 1001))) 
    
    print('4의 배수의 합 : ',sum(range(4, 1001, 4)))   

#Iterables 자료형 반복
#문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi']

for name in names:
    print(name)
    
# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

# 예제 3
word = 'Beautiful'

for s in word:
    print(s)
    
#예제 4
my_info = {
    "name" : "lee",
    "age" : 33,
    "city" : "seoul"
}

for k in my_info:
    print('key : ', k)

for v in my_info.values():
    print('key : ', v)
    
#예제
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
    
# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 78, 98]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break        
    else:
        print('Not Found: ', num)
        

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type: ", type(v))
    print("곱하기 2", v * 3)

# for -else
print()
for num in numbers:
    if num == 24:
        print("Found : 24")
        break
    
else: 
    print('Not Found : 24')
    
    
#구구단 
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()
    
# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('list', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))