#함수 정의 방법

#예제 1

from tkinter import Y


def first_func(w):
    print("Hello, ", w)
    
word = "GoodBoy"

first_func(word)

#예제2

def return_func(w1):
    value = "Hello, " +  str(w1)
    return value

x = return_func('goodboy2')
print(x)

# 예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)

#튜플 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul(10)
print(type(q), q, list(q))

print()
#튜플 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul(30)
print(type(p), p, set(p))

print()
#딕셔너리 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2' : y2, 'v3': y3}

d = func_mul(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

#중요중요
# *arg, **kwargs

#*arg(언팩킹)
def args_func(*args): #매개변수명은 자유
    
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
        
    print('-------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'kim' )
    
    
# **kwargs(언팩킹)

def kwargs_func(**kwargs):
    for v in kwargs.keys():
       print('Result : {}'.format(v), kwargs[v]) 
       
    print('-------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='cho')

# 전체 혼합
def example(args_1, arg_2, *aa , **kk):
    print(args_1, arg_2, aa, kk)

example(10, 20, 'lee', 'kim', 'park', 30, n1=30, n2=40, n3=50)

#중첩함수
def nested_func(num):
    
    def func_in_func(num):
        print(num)
        
    print("in func")
    func_in_func(num + 100)

nested_func(100)


#람다식 예제
#메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시 실행함수(heap 초기화) -> 메모리 초기화

def mul_func(x,y):
    return x*y

q = mul_func(10, 50)
print(q)

#람다 함수를 할당하는 예제
lambda_mul_func = lambda x,y :x*y
print(lambda_mul_func(50,50))

def func_final(x,y,func):
    print(x*y*func(100,100))

func_final(10,20, lambda x,y :x*y)
    

   
    
    
    
    