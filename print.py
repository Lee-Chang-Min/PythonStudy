print('Hello python')

#print 사용법, 기본출력
print('Hello python')
print("asdfasdf")
print() # 띄어 쓰기
print('''python Start!''')
print("""python Start!""")

#separator
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('010', '1234', '7777', sep='-')
print('python', 'google.com', sep='@')
print()

#end 옵션 -> 다음 print의 문자에 붙여준다
print('Welcom to', end=' ')
print('IT News', end=' ')
print('web site')
print()

#file 옵션
import sys
print
print('Learn Python', file = sys.stdout)

#format 사용(d: 3, s: 'python', f: 3.14)

print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', '2'))
print('{1} {0}' .format('one', 'two'))




