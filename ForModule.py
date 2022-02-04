
from test import count_prime1, count_prime2, count_prime2_1, count_prime3, count_prime_book
from test2 import seq_search, seq_search2, seq_search2_1, seq_search3, seq_search3_1, bin_search1

''' 검색 알고리즘을 위한 부분
tmp_list = []
for i in range(1000):
    tmp_list.append(i)
'''

import time
# 총 실행 시간을 저장할 변수
time_sum = 0
# 반복할 횟수를 저장할 변수
op_cnt = 1000  # operation_count : 실행 횟수

for idx in range(op_cnt):
    # 코드 실행 전, 현재 시각을 time1에 저장
    time1 = time.time()

    # 실행시간 테스트할 알고리즘
    count_prime3(10000)
    
    # 알고리즘 실행 이후 현재 시각(time.time())에서 아까 저장해놓은 실행전 시간 time1을 빼서
    # 알고리즘 실행 시간을 구해서 op_time 에 저장
    op_time = time.time() - time1
    
    # 총 실행시간을 구하기 위한 time_sum
    time_sum += op_time

    print(f"실행시간은 {op_time}입니다. ")
print(f"코드 반복 횟수는 {op_cnt}이며, 평균 실행시간은 '{time_sum / op_cnt}'초 입니다.")

