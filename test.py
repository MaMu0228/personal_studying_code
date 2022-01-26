import random
import time

"""
print("이름을 입력하세요. : ", end='')
name = input()
print(f"안녕하세요 {name}님. 반갑습니다. ")

age = int(input("당신의 나이를 입력하세요 :"))

print(f"당신의 나이는 {age}이고, 2진수로는 {bin(age)}", f"8진수로는 {oct(age)}, 16진수로는 {hex(age)}입니다.")

x = int(input("x에 넣을 숫자를 입력하시오 : "))
y = int(input("y에 넣을 숫자를 입력하시오 : "))

a = x if x > y else y

print(f"입력한 값중 더 큰 값은 {a}입니다. ")

"""

"""
print("학생의 수들의 점수를 모두 합쳐서, 합계와 평균을 알려주는 프로그램입니다.")
score = []
total = 0

num = int(input("학생의 수를 입력하시오"))
for i in range(num):
    score.append(int(input(f"{i}번째 학생의 점수를 입력하시오: ")))
    total += score[i]
print(f"총 점수는 {total}이며, 평균 점수는 {(total / num)}입니다.")
print(f"맨 뒤 학생들로부터의 점수는 {score[-1]}, {score[-2]}, {score[-3]}, {score[-4]}, {score[-5]}입니다.")

"""

"""
list04 = list() ---> list04 = []와 같음
list05 = list('abc') ---> a, b, c란 문자들이 들어있는 3크기 리스트생성후 list05에 넣음
list06 = list([1, 2, 3]) ---> 1, 2, 3이 들어있는 리스트에서 1, 2, 3을 빼서 리스트를 만들어 list06에 넣음
list07 = list((1, 2, 3)) ---> 1, 2, 3이라는 튜플에서 1, 2, 3을 빼서 리스트로 만들어 list07에 넣음
list08 = list({1, 2, 3}) ---> 1, 2, 3집합에서 1, 2, 3을 빼서 리스트를 만들어 list08에 넣음

list12 = [None] * 5 ---> [None, None, None, None, None]이 들어있는 리스트 생성

튜플은 반드시 ','가 붙어야함
tuple01 = () ---> 빈 튜플
tuple02 = 1, ---> 1만 들어있는 튜플
tuple02-1 = 1 ---> 그냥 1이 들어있는 tuple02-1이란 변수
tuple02-2 = (1, ) ---> 1이 들어있는 튜플
tuple02-3 = (1) ---> 1이 들어있는 tuple02-3이란 변수
tuple3 = 'a', 'b', 'c' ---> ('a', 'b', 'c')이 들어있는 튜플

list = [1, 2, 3]
a, b, c, = list ---> list안에 들어있는 1, 2, 3을 차례대로 a, b, c에 넣음 ---> 이걸 unpack 이라함
list[2] ---> 3번째로, 여기서의 값은 3
list[-1] ---> 뒤에서 1번째로, 여기서의 값은 3

s = [11, 22, 33, 44, 55 ,66]
s[0:6] ---> s 리스트에 담긴 원소중 0번 인덱스부터 6번 인덱스 전까지를 잘라서 꺼내라
s[2:3] ---> s 리스트에 담긴 원소중 2번 인덱스부터 3번 인덱스 전까지를 잘라서 꺼내라
s[0:6:2] ---> s 리스트에 담긴 원소중 0번 인덱스부터 6번 인덱스 전까지를 2개씩 건너뛰어 잘라 꺼내라

s[:] ---> 리스트 s의 모든 원소를 출력해라
s[:n] ---> 리스트 s의 처음부터 인덱스 n 전까지를 잘라서 꺼내라
s[i:] ---> 리스트 s의 i 인덱스부터 끝까지를 잘라서 꺼내라
s[-n:] ---> 리스트의 -n(끝에서 n번째)부터 끝까지를 잘라서 꺼내라
s[::k] ---> 리스트의 맨처음부터 끝까지를 k개씩 뛰어서 꺼내라
s[::-1] ---> 리스트를 맨 끝에서부터 처음까지를 꺼내라(순서 정반대로 바꾸기)

len(x) ---> x 리스트나 튜플의 원소개수
min(x), max(x) ---> x 리스트나 튜플이 가진 최댓값 원소나 최솟값 원소 


"""

""" if __name == "__main__" 예시
if __name__ == '__main__':
    s = [11, 22, 33, 44, 55, 66, [10, 20], "아잉"]  # 리스트는 처음에 개수를 정해야함, 그래서 추가할 시 list.append()를 써야함
    print(f"{s[0:6]}, {s[2:3]}, {s[0:7]}, {s[::-1]}")
    print(f"s 리스트에 들어있는 원소 개수는 : {len(s)}, 합은 {sum(s[0:6])}입니다.")
"""

"""
# 리스트가 비지 않았을 때랑 비었을 때를 간단히 표현하는 방법
while True:
    # 조건에 리스트 변수를 넣을 경우, 리스트가 비어있지 않다면
    if s:
        print(f"리스트에서 값을 빼려면 '-'를 입력하시오 : ")
        if input() == '-':
            print(f"{s.pop()}")
        else:
            print(f"-를 입력해주세요.")
    # 리스트가 비었다면
    else:
        print(f"리스트가 비었습니다.")
        break
# """

"""
numbers = range(10000)
# 만약 리스트의 구성 원소가 홀수면, 값을 2배해서 리스트에 저장후, 최종 리스트를 넣어라
start = time.time()
twice = [num * 2 for num in numbers if num % 2 == 1]
print(f"twice 총 실행시간 {time.time() - start}")

# 리스트의 구성원소들 각각에 3배를 해서 리스트에 저장후, 최종 리스트를 넣어라
twice2 = [num * 3 for num in numbers]
# []를 감싸면 무조건 리스트, ','을 붙이면 무조건 튜플

# twice와 같은 기능이지만 훨씬 김, 계산 속도는 똑같다
start2 = time.time()
twice3 = []
for num in numbers:
    if num % 2 == 1:
        twice3 += [num * 2]
print(f"twice3의 총 실행시간 {time.time() - start2}")
print(f"{twice}, {twice2}, {twice3}")
# """

"""
from typing import Any, Sequence

def max_of(a : Sequence) -> Any:  # a라는 변수는 연속형 자료형(Sequence)을 받고, 제약없이 아무 자료형으로(Any) 반환하겠다
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum  # -> Any 때문에 만약 리스트 안에 들어있는 값이 int든 float든 모두 반환가능

# 실행되는 모듈이 들여쓰기가 없는 메인 모듈일 때 실행해라, 즉 메인코드를 실행중일 때만 실행해라
if __name__ == '__main__':
    print("배열의 최댓값을 구합니다. ")
    num = int(input("원소의 수를 입력하세요: "))
    x = [None] * num  # num 숫자만큼 None 으로 리스트 초기화

    for i in range(num):
        x[i] = int(input(f"x[{i}]값을 입력하세요: "))

    print(f"최댓값은 {max_of(x)}입니다.")

# """

"""
t = (4, 7, 5.6, 2, 3.14, 1)
s = "string"
a = ["DTS", "AAC", "FLAC"]

print(f"{t}의 최댓값은 {max(t)}입니다.")  # 숫자들이 들어있는 컨테이너에선 무조건 큰 수가 최댓값
print(f"{s}의 최댓값은 {max(s)}입니다. ")  # 문자열에서 가장 큰 값은 제일 알파벳순서에서 나중에 나오는 알파벳
print(f"{a}의 최댓값은 {max(a)}입니다. ")  # 문자열이 들어있는 리스트에서 가장 큰 값은 사전순으로 나중에 나오는 문자열

# """

""" enumerate(x)와 enumerate(x, 정수) 사용법

x = ["John", "George", "Paul", "Ringo"]

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")

for i, name in enumerate(x):
    print(f"{name}는 {i} 번째에 있습니다.")

for i, name in enumerate(x, 1):
    print(f"{i}번째 = {name}")

# """

"""
from typing import Any, MutableSequence

def reverse_array(arr: MutableSequence) -> None:
    # 뮤터블 시퀸스(변경 가능한 배열)의 원소를 받고 역순으로 정렬해 
    # 반환하는 함수

    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i -1] = arr[n - i - 1], arr[i]

def reverse_array2(arr: MutableSequence) -> None:
    # 내가 변현항 배열의 순서를 역순으로 바꾸는 함수
    n = len(arr)
    for i in range(n):
        arr[i] = arr[-i]

if __name__ == "__main__":
    print("배열을 역순으로 정렬합니다. ")
    num = int(input("원소의 개수를 입력하세요 : "))
    list_x = [None] * num

    for i in range(num):
        list_x[i] = random.random() % 10  # random 함수를 다시 알아보고 고치기
    start1 = time.time()
    reverse_array(list_x)
    print(f"reverse_array를 사용한 계산 속도는 {time.time() - start1}입니다.")
    print(f"reverse_array 방식의 결과는 {reverse_array(list_x)} 입니다.")

    start2 = time.time()
    reverse_array2(list_x)
    print(f"reverse_array를 사용한 계산 속도는 {time.time() - start2}입니다.")
    print(f"reverse_array 방식의 결과는 {reverse_array2(list_x)} 입니다.")

# """

"""5
from typing import Any, MutableSequence

def reverse_array(a : MutableSequence) -> MutableSequence:
    # 뮤터블 시퀸스 a의 원소(리스트)를 역순으로 정렬해서 반환하는 함수 
    n = len(a)  # 변환 가능한 연속형 컨테이너의 크기를 저장해서 최대 인덱스로 사용
    rev_a = list(a)  # 파이썬의 대입은 같은 객체를 가리키는 이름만 바꾸는 것이므로, 새로운 객체를 만들려면 list()나 tuple()처럼 새로 만들어 대입해야한다.
    for i in range(n // 2):
        rev_a[i], rev_a[n - i -1 ] = rev_a[n - i -1], rev_a[i]
    return rev_a

if __name__ == "__main__":
    print('배열 원소를 역순으로 정렬합니다. ')
    nx = int(input("원소의 수를 입력하시오 : "))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input("원소에 넣을 값을 입력하시오 : "))

    rev_x = reverse_array(x)
    print(f"원래의 배열은 {x}이며, 순서가 바뀐 배열은 {rev_x}입니다.")
# 5"""

"""6
x = int(input("원하는 리스트 크기를 입력하시오 : "))
list1 = []
for _ in range(x):
    list1.append(random.randint(1,100))

print(f"현재 생성된 리스트는 {list1}입니다. ")
rev_list1 = list(reversed(list1))
list1.reverse()
print(f"현재 .reverse()를 쓴 리스트의 값은 {list1}입니다. \n reversed()를 써서 만든 값은 {rev_list1}입니다. ")
#  *** list.reverse()는 리스트 값 자체를 변경해버리니, 새로운 객체를 만드는 list(reversed(x))를 좀 더 많이 쓰자 ***

# 6"""

"""7
def card_conv(num : int, notation :int) -> str:
    # 정수 num을 받고 notation_num 진수로 변환한다음 그 수를 나타내는 문자열로 반환
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    notation_s = len(str(notation))

    print(f"{notation:2} | {num:{notation_s}d}")

    # num 이 양수가 아닐 때까지 반복
    while num > 0:
        print("    +" + (notation_s + 2) * '-')
        if num // notation:
            print(f"{notation:2} | {num // notation} ....{num % notation}")
        else:
            print(f"    {num // notation:{num}d} .... {num % notation}")
        d += dchar[num % notation]  # dchar 문자열에서 정수를 진수로 나누고 나온 나머지의 순서 문자를 d에 더해서 넣음
        num //= notation  # num 정수를 notation_num 진수로 나눠서 나온 몫을 num에 저장
        # print(f"d = {d}, num = {num}, dchar[{num % notation_num}] = {dchar[num % notation_num]}")
    return d, d[::-1]  # 저장한 d의 문자열의 순서를 정반대로 바꿔서 반환


#"""

'''8
if __name__ == "__main__":
    print("10진수를 n진수로 변환합니다. ")

    while True:
        while True:
            num = int(input("변환할 음이 아닌 정수를 입력하세요 : "))
            if num > 0:
                break
        while True:
            notation = int(input("변환할 진수를 입력하세요 (2진수 ~ 36진수까지 가능): "))
            if 2 <= notation <= 36:
                break

        print(f"{notation}진수로 변환한 값은 {card_conv(num, notation)}입니다. ")
        retry = input("한 번 더 변환할까요? (Y/N) :")
        if retry in ['N', 'n']:
            break
# '''

'''9
# 뮤터블인 list를 인수로 받으면, 기존 인수에 값을 넣지만
# 임뮤터블인 사전이나 튜플을 넣으면, 새로운 객체를 넣고 반환함
def change(lst, idx, val):
    """ 리스트, 순서, 값을 넣으면, 리스트의 순서에 값을 넣어주는 함수 """
    lst[idx] = val

x = [11, 22, 33 ,44 ,55]
y = (1, 2, 3, )
print(f"리스트 x = {x}, {type(x)}")
# 튜플은 변환이 안되기에, 이 코드는 에러가 발생
print(f"튜플 y = {y}, {type(y)}")

index = int(input("삽입할 인덱스 순서를 입력하세요 : "))
value = int(input("리스트에 넣을 값을 입력하세요 : "))

change(x, index, value)
change(y, index, value)
print(f"x = {x}")
print(f"y = {y}")
# '''

# '''10, for문을 이용해 단순히 소수 구하는 함수
# n을 n 이하의 수들로 모두 나눳을 때 한번이라도 0으로 나눠 떨어지면 소수가 아님

def count_prime1(number):
    # op_time = time.time()  # operation_time : 실행 시간
    op_cnt = 0  # operation_count : 실행 횟수
    primes = []  # primes : 소수들

    # 2부터 number 의 수까지 n에 들어감
    for n in range(2, number + 1):
        # n이 10이라면, i는 2부터 9까지의 수로 한번씩 나눔
        for i in range(2, n):
            # 계산할 때마다 counter 증가
            op_cnt += 1
            # 만약 n을 i로 나눴을 때 나머지로 0이 나온다는 것은 나눠진다는 것이니 소수가 아님
            if n % i == 0:
                break
        else:
            primes.append(n)
    # print(f"총 실행시간 : {time.time() - op_time}")
    print(f"나눗셈을 한 횟수 : {op_cnt}")
    print(f"2~ {number} 이하에서의 소수의 갯수 : {len(primes)}")
    return primes

# '''

# '''11, 소수를 넣은 배열을 이용해 좀 더 빠르게 소수를 구하기, 이전보다 약 5배 빠름
# 소수는 2빼고 모두 홀수라는 것을 이용해 계산을 좀 더 빠르게
def count_prime2(number):
    cnt = 0
    prime_cnt = 0
    primes = [None] * 1000

    # primes 리스트에 첫 소수인 2를 넣고, 2를 넣었으니 prime_cnt를 1 증가
    primes[0] = 2
    prime_cnt += 1

    # 3부터 1001까지 2칸씩이니, 3부터 시작하는 홀수만 계산하겠다
    # 왜냐면, 짝수는 무조건 나눠떨어지니까! 소수는 2빼고 홀수다
    for n in range(3, number + 1, 2):
        # 1부터 prime_cnt 개수까지만 실행하겠다.
        for i in range(1, prime_cnt):
            # 나눈 횟수 1증가
            cnt += 1
            # 만약 primes 리스트에 있는 값들로 나눠서 0이 나온다 --> 소수가 아니니 그냥 넘어간다
            if n % primes[i] == 0:
                break
        # 만약 0으로 나눠지지 않는다면, 그 수를 primes 리스트의 현재 인덱스에 넣어라.
        else:
            primes[prime_cnt] = n
            # 소수 개수를 추가했으니 prime_cnt 개수 1 증가
            prime_cnt += 1
    print(f"나눗셈을 실행한 횟수 : {cnt}")
    print(f"찾은 소수의 개수 : {prime_cnt}")

# 11'''

'''12책에 써 있던 소수 구하는 제일 빠른 알고리즘, 위보다 계산 속도는 약 2배 빠름
start12 = time.time()
cnt = 0 # 계산 횟수
found_pn = 0 # 찾은 소수의 개수
primes = [None] * 1000 # 소수를 저장할 배열, 2를 제외한 짝수는 소수가 아니기에 절반값인 500으로도 충분하다

# 소수 배열인 primes의 인덱스 0에는 2를 넣고, 넣었으니 카운트 1 증가
primes[found_pn] = 2
found_pn += 1
# 소수 배열의 primes의 인덱스 1에 3을 넣고, 카운트 1 증가, 왜냐면 2와 3은 소수니까
primes[found_pn] = 3
found_pn += 1

# 2와 3은 이미 위에서 계산했으니 5부터 1000까지 계산하되, 똑같이 소수는 2빼곤 모두 홀수니 2칸씩 뛰면서 계산한다.
for n in range(5, 2001, 2):
    i = 1
    # 배열 1(3)의 제곱을 한 값이 현재의 n보다 작거나 같으면
    while primes[i] * primes[i] <= n: 
        # "primes[i] * primes[i]" 라는 계산과 "n % primes[i]"계산을 하니, 총 계산 횟수는 2 증가
        cnt += 2
        # 만약 현재 n을 현재 배열값으로 나눴을 때 0이 나온다면 종료
        if n % primes[i] == 0:
            break
        # 그리고 현재 숫자가 소수인지 아닌지 이미 확인했으니, 다시 1 증가
        i += 1
    else:
        # 만약 현재 배열에 들어있는 값의 제곱이 n보다 작다면, 소수이므로 소수 번호를 인덱스 삼아 배열 primes 에 저장
        primes[found_pn] = n
        # 소수를 추가했으니, 소수 카운트 1 증가
        found_pn += 1
        # 만약 "primes[i] * primes[i] <= n"조건이 만족하지 않을 경우, 자체 계산 횟수밖에 없으니 1증가
        cnt += 1
print(f"12:찾은 소수 : {primes}")
print(f"12: 총 실행 시간 : {time.time() - start12}")
print(f"12:곱셈과 나눗셈을 실행한 횟수 : {cnt}")
print(f"12:찾은 소수의 개수 : {found_pn}")
# 12'''

# '''13 내가 만든 최신 소수 구하는 알고리즘
# 책에 써져있는 것보다 약 최소 2배~ 최대9배가 빠르다
# 제곱근 + 소수는 2빼고 모두 홀수를 이용
# 개량버전


def count_prime3(number):
    cnt = 0
    primes = [2, 3]
    # (정보) 루트 n보다 작은 소수들로 n을 나눴을 때, 모두 나눠 떨어지지 않으면 n은 소수다
    for q in range(5, 2001, 2):
        i = 1  # 3부터 시작
        # 소수가 담긴 배열에서 소수를 꺼내서, 소수의 제곱이 판단할 q보다 작을경우 while문 실행하다, 조건이 안 맞을시 else 실행
        while primes[i] * primes[i] <= q:
            cnt += 2
            if q % primes[i] == 0:
                break
            i += 1
        # while 문의 조건이 부정되는 순간 else문 실행
        else:
            primes.append(q)
    # print(f"13:찾은 소수ex : {primes}")
    print(f"13:곱셈과 나눗셈을 실행한 횟수ex : {cnt}")
    print(f"13:찾은 소수의 개수ex : {len(primes)}")
    # print(f"i : {i}")


def count_prime3_1(number):
    cnt = 0
    primes = [2, 3]
    # (정보) 루트 n보다 작은 소수들로 n을 나눴을 때, 모두 나눠 떨어지지 않으면 n은 소수다
    for q in range(5, 2001, 2):
        i = 1  # 3부터 시작
        # 소수가 담긴 배열에서 소수를 꺼내서, 소수의 제곱이 판단할 q보다 작을경우 while문 실행하다, 조건이 안 맞을시 else 실행
        while primes[i] ** 2 <= q:
            cnt += 2
            if q % primes[i] == 0:
                break
            i += 1
        # while 문의 조건이 부정되는 순간 else문 실행
        else:
            primes.append(q)
    # print(f"13:찾은 소수ex : {primes}")
    print(f"13:곱셈과 나눗셈을 실행한 횟수ex_1 : {cnt}")
    print(f"13:찾은 소수의 개수ex : {len(primes)}")
    # print(f"i : {i}")


# 13'''

#############


'''14 미리 알고 있는 소수들을 모두 배열에 넣고, 모르는 소수부터 계산 시작하면 좀 더 빠름

start14 = time.time()
cnt = 0
primes = [2, 3, 5, 7, 11, 13]
found_pn = 6 # 2와 3의 소수를 이미 리스트에 넣고 시작하니, 소수 카운트도 2부터 시작
# (정보) 루트 n보다 작은 소수들로 n을 나눴을 때, 모두 나눠 떨어지지 않으면 n은 소수다
for q in range(17, 2001, 2):
    i = 1 # 3부터 시작
    # 소수가 담긴 배열에서 소수를 꺼내서, 소수의 제곱이 판단할 q보다 작을경우 while문 실행하다, 조건이 안 맞을시 else 실행
    while primes[i] * primes[i] <= q:
        cnt += 2
        if q % primes[i] == 0:
            break
        i += 1
    # while 문의 조건이 부정되는 순간 else문 실행
    else:
        found_pn += 1
        primes.append(q)
print(f"14:총 실행 시간 : {time.time() - start14}")
print(f"14:찾은 소수 : {primes}")
print(f"14:곱셈과 나눗셈을 실행한 횟수 : {cnt}")
print(f"14:찾은 소수의 개수 : {found_pn}")
print(f"i : {i}")

# 14'''


