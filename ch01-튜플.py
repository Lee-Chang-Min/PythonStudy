#튜플 자료형(순서o, 중복o, 수정x, 삭제x) #불변

#선언 
a = (1,) #튜플로 선언 되고 싶으면 끝에 ,가 있어야함
b = (1, 2)
c = (11, 12, 13, 14)
d = (100, 1000, 'ace', 'base', 'captine')
e = (100, 1000, ('ace', 'base', 'captine'))

print(type(a),type(b))

#인덱싱
print('>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 수정x
#d[0] = 1500

#슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

#튜플 연산
print('>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

#튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(3))

# 팩킹 & 언팩킹(packing and unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'quz')
print(t)
print(t[0])

#언팩킹 1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

#팩킹 & 언팩킹
t2 = 1, 2, 3
t3  = 4
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

