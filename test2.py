import time
import test
import random
import copy
from typing import Any, Sequence

"""------------------
print("1부터 입력받은 n까지의 수를 모두 더해서 출력하는 함수입니다.")
n = int(input("n값을 입력하세요 : "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
    print(f"수작업으로 구한 현재까지의 sum 값은 {int(sum)}입니다. ")

sum = 0

for i in range(1, n + 1):
    sum += i
    i += 1
    print(f"for문으로 구한 현재까지의 sum 값은 {int(sum)}입니다. ")


sum = n*(n+1)//2
print(f"가우스 덧셈으로 구한 합은 {int(sum)}입니다.")
---------------------"""

"""--------------------------
print("a와 b값을 입력받고, 입력받은 두 값중 작은 값부터 큰 값까지의 합을 구하는 프로그램입니다. ")
a = int(input("a의 값을 입력하세요 : "))
b = int(input("b의 값을 입력하세요 : "))

if a > b:
    a, b = b, a

sum = 0
for i in range(1, b + 1):
    sum += i
    print(f"현재 까지 계산된 값은 {sum}입니다. ")
 --------------------------- """

# 별로 좋지 않은 코딩
"""

print("+-을 번갈아가며 출력하는 프로그램입니다.")
n = int(input("얼마나 반복하시겠습니까? : "))

start = time.time()
for i in range(n + 1):
    if i % 2:
        print("-", end="")
    else:
        print("+", end="")
print(f"\n실행 시간은 {time.time() - start}입니다.")
# """
# 좀 더 좋은 코딩
"""


print("+-를 번갈아가며 출력하는 프로그램입니다. ")
n = int(input("몇 개를 출력하시겠습니까? :"))

start = time.time()
for _ in range(n // 2):
    print('+-', end="")

if n % 2:
    print('+', end='')
print()
print(f"\n실행 시간은 {time.time() - start}입니다.")

# """

# ---비효율적 코드---
"""
print("*를 출력합니다. ")
n = int(input("몇 개를 출력할까요? : "))
w = int(input("몇 개마다 줄바꿈을 할까요?: "))

start = time.time()

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()
if n % w:
    print()
print(f"총 실행 시간은 {time.time() - start}입니다.")
# """

# ---효율적 코드---
"""

print("*를 출력합니다")
n = int(input("몇 개를 출력할까요? :"))
w = int(input("몇 개마다 줄바꿈을 할까요? :"))

start = time.time()

# 총 개수를 줄 바꿈을 할 개수로 나누고, 나온 수 만큼 반복
for _ in range(n // w):
    # 그리고 줄 바꿈 개수만큼을 반복
    print('*' * w)
    
# 전체 개수를 줄바꿈할 개수로 나누고 나온 나머지가 0이 아니라면, 
# 당연히 0이 아닌만큼을 추가해준다
rest = n % w
if rest:
    print('*' * rest)

print(f"총 실행 시간은 {time.time() - start}입니다.")


# """

"""
print("배열의 최댓값을 구하는 프로그램입니다. ")
print("주의 : 'End'를 입력하면 종료합니다. ")

number = 0
x = []

while True:
    s = input(f"x[{number}]값을 입력하세요. :")
    if s == "End":
        break
    x.append(int(s))
    number += 1
print(f"{number}개 입력하셨습니다. ")
print(f"최댓값은 {test.max_of(x)}입니다. ")

# end_comment """

'''1
number = 0
list1 = []
print("실수를 검색합니다. ")
print("!주의 : 'end'를 입력하면 종료됩니다. ")

while True:
    s = input(f"x[{number}]: ")
    if s == "end":
        break
    list1.append(float(s))
    number += 1

key = float(input('검색할 값을 입력하세요. : '))
idx = seq_search(list1, key)
print(f"{list1}")
if idx == -1:
    print(f"찾고자 하는 값이 콘테이너에 없습니다. ")
else:
    print(f"찾고자 하는 값은 {idx}에 있습니다.")

# 1'''


###############
# '''15

# 단순 선형 검색 알고리즘 1
def seq_search(container: Sequence, key: Any) -> int:
    tmplist = copy.deepcopy(container)

    """
    (콘테이너, 찾고자 하는 값) --> 콘테이너 몇 번째 인덱스에 있는지 반환하는 함수
    """
    for idx, i in enumerate(tmplist):
        if i == key:
            return idx
    else:
        return -1
# 15'''
#################


'''2


tuple1 = (4, 7, 5.6, 2, 3.14, 1)
str1 = "string"
list1 = []
for i in range(3001):
    list1.append(i)

print(f"{tuple1}에서 5.6의 인덱스는 {seq_search(tuple1, 5.6)}입니다.")
print(f"{str1}에서 'n'의 인덱스는 {seq_search(str1, 'n')}입니다. ")
print(f"{list1}에서 'DTS'의 인데그는 {seq_search(list1, 'DTS')}입니다.")

# 2'''

# '''3

# 2는 1보다 약 13배 빠름
def seq_search2(seq: Sequence, key: Any) -> int:
    tmplist = copy.deepcopy(seq)
    tmplist.append(key)

    i = 0
    while True:
        if tmplist[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

# 2_1은 1보다 약 10%에서
def seq_search2_1(seq: Sequence, key: Any) -> int:
    tmplist = copy.deepcopy(seq)
    tmplist.append(key)

    i = 0
    while tmplist[i] != key:
        i += 1
    return -1 if i == len(seq) else i

# 3은 2보다 약 2배 느림
def seq_search3(seq: Sequence, key: Any) -> int:
    tmplist = copy.deepcopy(seq)
    # tmplist.append(key)

    for idx, val in enumerate(seq):
        if val == key:
            return idx
    return -1

# 3은 2보다 약 2배 느림
def seq_search3_1(seq: Sequence, key: Any) -> int:
    tmplist = copy.deepcopy(seq)
    tmplist.append(key)

    for idx, val in enumerate(seq):
        if val == key:
            return idx
    return -1


if __name__ == "__main__":
    time1 = time.time()
    print(f"list1에서 1함수를 이용한 {seq_search(list1, 2990)}입니다. \n 실행 시간 : {time.time() - time1}")
    time2 = time.time()
    print(f"list1에서 2함수를 이용한  {seq_search2(list1, 2990)}입니다. \n 실행 시간 : {time.time() - time2}")
    time2_1 = time.time()
    print(f"list1에서 2_1함수를 이용한  {seq_search2_1(list1, 2990)}입니다. \n 실행 시간 : {time.time() - time2_1}")
    time3 = time.time()
    print(f"list1에서  3함수를 이용한  {seq_search3(list1, 2990)}입니다. \n 실행 시간 : {time.time() - time3}")
# 3'''


# """ 이진검색 1
def bin_search1(c: Sequence, key: Any) -> Any:
    first = 0
    last = len(c) - 1  # 인덱스는 전체 길이의 -1까지이니
    while True:
        mid = (first + last) // 2
        # 만약 리스트 가운데값이 key와 같으면, 현재 mid의 숫자 반환
        if c[mid] == key:
            return mid
        # 만약 리스트 중앙값이 키보다 작으면, first에 mid보다 1큰 숫자를 저장
        elif c[mid] < key:
            first = mid + 1
        # 만약 리스트 중앙값이 키보다 크면, last에 mid보다 1 작은 값을 저장
        else:
            last = mid - 1
        # 만약 첫 인덱스가 마지막보다 커진다면, 말이 안되므로 강제 종료
        if first > last:
            break
        return -1


# 이진 검색 1 """

