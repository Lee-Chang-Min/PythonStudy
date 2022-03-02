#파이션 딕셔너리
#범용적으로 가장 많이 사용
#딕셔너리 자료형(순서X, 키 중복X, 수정o, 삭제o)

# 선언 
a = {
        'name': 'Kim',
        'phone' : '01033337777',
        'birth' : '870514'
     }

b = {0: 'Hello python'}
c = {'arr' : [1,2,3,4]}
d = {
     'name' : 'niceman',
     'city' : 'seoul',
     'age' : 33,
     'grade' : 'a',
     'status' : True
}

e = dict([
    ('name', 'niceman'),
    ('DSD', 'niceman') 
]) 

f = dict(
    name = 'niceman',
    city = 'seoul',
    age = 33,
    status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

#출력
print('a - ', a['name']) #존재x -> 에러발생
print('a - ', a.get('name1')) #존재x -> none 처리 좀더 안정적으로 개발 할수 있음
print('b - ', b[0]) 
print('b - ', b.get(0)) 

print('f - ', f.get('city'))
print('f - ', f.get('age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

#딕셔너리 추가
print('a - ', len(a))
print('a - ', len(b))
print('a - ', len(c))
print('a - ', len(d)) # 키의 갯수를 세는것

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())