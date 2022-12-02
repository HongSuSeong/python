"""
# 정수형
a = 1000 # 양의 정수

a = -7 # 음의 정수

a = 0 # 0

# 실수형
a = 157.93 # 양의 실수

a = -1837.2 # 음의 실수

a = 5. # 소수부가 0일때 0을 생략

a = -.7 # 정수부가 0일때 0을 생략

# 실수 의 지수표현
a = 1e9 # 1000000000 10억

a = 75.25e1 # 752.5

a = 3954e-3 # 3.954

# 실수 계산시 오차

a = 0.3 + 0.6  # 0.8999999999999999
a

if a == 0.9:
    print(True)
else:
    print(False)

# 해결 방안 round() 함수를 이용한다.
# 두 개의 인자를 받는데 첫번째는 실수형 데이터 두번째는 (반올림하고자하는 위치 -1)
round(1223.2242355,4)


#수 자료형 연산

a,b = 7,3

a/b # 나누기

a%b # 나머지

a//b # 몫

a ** b # 거듭제곱

#리스트 자료형
# 인덱스 0부터 시작
a = [1,2,3,4,5,6,7,8,9]

a[4] # 다섯번째 원소

# 빈 리스트 선언 두가지 방법
a = list()  # 1
a = []      # 2

# N 인 1차원 리스트 초기화시 편한방법
#ex)크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n

# 인덱싱 == 인데스값을 입력하여 리스트의 특정한 원소에 접근 하는것
a = [1,2,3,4,5,6,7,8,9]
a[-1] # 뒤에서 첫 번째 원소

a[-3] # 뒤에서 세 번째 원소

a[3] = 7 # 앞에서 세 번째 값 7로 변경

# 슬라이싱 == 연속적인 위치를 갖는 원소들을 가져올때 하는것
a = [1,2,3,4,5,6,7,8,9]

a[1:4] # 두번째부터 네번째원소까지

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]

아래 내용이 위와 같다.
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)


# 1부터 9까지 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]

# n * m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)] # _ 언더바의 역할 반복을 위한 변수의 값을 무시하고자 할때 사용된다.
array[1][1] = 5
# [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]

# 2차원 리스트 초기화시 반드시 리스트 컴프리헨션을 이용 아래내용은 문제발생
n = 3
m = 4
array = [[0] * m] * n
array[1][1] = 5
# [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]


리스트 관련 메서드
## : 자주 사용
## append 삽입
## insert 특정한 인덱스 위치에 원소를 삽입 insert(삽입할 위치 인덱스 , 삽입할 값)
## remove 특정한 값을 갖는 원소를 제거  remove(3) 값이 3인 데이터 삭제
sort 오름차순 정렬 sort(reverse=True) 내림차순 정렬
reverse 모든 순서를 뒤집는다
count 특정한 값을 가지는 데이터 개수 count(3) 값이 3인 데이터 개수

# remove를 여러개 하고 싶을때
a = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set] # [1, 2, 4]

#문자열 자료형
data = 'Hello World'

data = "Don't you know \"Python\"?"

a = "Hello"
b = "World"
a+b # HelloWorld

a = "String"
a*3 # StringStringString

a = "ABCDEF"
a[2:4] # CD

# 튜플 자료형
# 변경되지 않음 - 그래프 알고리즘을 구현할때 자주사용된다.
a = (1,2,3,4)

#사전 자료형
# 키와 값 쌍을 가진 데이터 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

data.keys() # 키만 뽑기
data.values() # 값만 뽑기

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 집합 자료형
# 중복 X , 순서 X
data = set([1,1,2,3,4,4,5]) # 초기화 방법 1

data = {1,1,2,3,4,4,5} # 초기화 방법 2

# 집합 자료형 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

a | b # 합집합
a & b # 교집합
a - b # 차집합

# 집합 자료형 함수
data = set([1,2,3])

data.add(4) # 새로운 원소 추가

data.update([5,6]) # 새로운 원소 여러개 추가

data.remove(3) # 3이라는 원소 제거

#조건문

x = 15

if x>=10:
    print(x)


score = 85
if score >=90:
    print("학점: A")
elif score >=80:
    print("학점: B")
elif score >=70:
    print("학점: C")
else:
    print("학점: F")

score = 85

if score >= 70:
    print("성적이 70점 이상입니다.")
    if score >= 90:
        print("우수한 성적입니다.")
else:
    print("성적이 70점 미만입니다.")
    print("조금 더 분발하세요.")

print("프로그램을 종료합니다.")

# 비교연산자

x == y
x != y
x > y
x < y
x >= y
x <= y



# 논리 연산자


x and y
x or y
not x




# 기타 연산자


x in 리스트
x not in 문자열


# 조건문 아무것도 처리하고 싶지 않을때 pass
score = 85

if score >= 70:
    pass # 나중에 작성할 소스코드
else:
    print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다.")

# 조건문 표현방식 한 줄일때
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

score = 70
result = "Success" if score >= 80 else "Fail"

a = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]

print(result)

# 반복문
# while문
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# for문
result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10): # range(시작값, 끝값+1)
    result += i
print(result)


scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

scores = [90, 85, 77, 65, 97]
cheating_list = {2,4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x",j,"=",i*j)
    print()

# 함수
def add(a,b):
    return a + b
add(3,5)

def add(a,b):
    print('함수의 결과',a + b)
add(3,5)
add(b=4, a=3)

# 글로벌 변수
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다 표현식
print((lambda a, b: a + b)(3, 7))

# 입출력
n = int(input()) # 단 건
data = list(map(int, input().split())) # 여러 건
data.sort(reverse = True)
print(data)

n,m,k = map(int, input().split())

print(n,m,k)

import sys
data = sys.stdin.readline().rstrip()



a = 1
b = 2
print(a, b)
print(a)
print(b)

answer = 7
print("정답은 " + str(answer) + "입니다.")

answer = 7
print("정답은", str(answer), "입니다.")

answer = 7
print(f"정답은 {answer}입니다.")


# 내장함수
# 더하기
result = sum([1,2,3,4,5])
print(result)

# 작은거
result = min(7,3,5,2)
print(result)


# 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3+5)*7")
print(result)


# 정렬 오름차순
result = sorted([9,1,8,5,4])
print(result)

# 정렬 내림차순
result = sorted([9,1,8,5,4], reverse = True)
print(result)


# 람다식을 이용한 정렬
result = sorted([('홍길동',35),('이순신',75),('아무개',50),('강슬기',29)], key = lambda x: x[1], reverse = True)
print(result)

data = [9,1,8,5,4]
data.sort()
print(data)

라이브러리

# itertools  반복되는 데이터를 처리하는 기능
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# combinations
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data,2))
print(result)


# product
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data,repeat=3))
print(result)



from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2))
print(result)

"""