# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) 

# 빈 문자열
str_t1 = ''
str2_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str2_t2), len(str_t1))

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")

print('a \t b')
print('a \n b')

escape_str1 = "Do you have a \" retro game\"?"
print(escape_str1)

#탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "new Line \n check!"
print(t_s1)
print(t_s2)

#Row String 
raw_s1 = r'D:\python\test' #역슬래쉬를 있는 그래도 표현할수 있음(소문자 r을 통해서)
print(raw_s1)
print()

#멀티라인 입력
mult_str = \
"""
sdafsdf
asdfasdfasdf
asdfasdfasdfasdf
"""
print(mult_str)

#문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "how are you doing"
str_o4 = "seoul deajeon busan Jinji"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upeer, isalnum, startswith, count, endswith, isalpha..)

print("Capitalize: ", str_o1.capitalize()) #첫번째 시작글자를 대문자로 바꿔준다
print("endswith?: ", str_o2.endswith("e")) # 마지막글자의 유효성 검사
print("replace: ", str_o1.replace("thon", 'Good'))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' ')) #특정 단위를 분리할때

#반복(시퀀스)
im_str = "Good boy!"

print(dir(im_str)) # __iter__

#출력
for i in im_str:
    print(i)
    
#슬라이싱 연습
str_s1 = "Nice Python"

#슬라이싱 연습
print(len(str_s1))
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) #[5:11]
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])

print(str_s1[1:4:2])# 1번 인덱스부터 4개가져오는데 2개씩 건뛰면서

print()
print(str_s1[-5:]) # -는 뒤부터 시작
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

#아스키 코드(또는 유니코드)
print("아스키 코드 ==============")
a = 'z'
print(ord(a)) # 아스키코드로
print(chr(122)) #문자로 