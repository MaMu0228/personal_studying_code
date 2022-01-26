import time
from test import count_prime1, count_prime2, count_prime3, count_prime3_1
from test2 import seq_search, seq_search2, seq_search2_1, seq_search3, seq_search3_1, bin_search1

tmp_list = []
for i in range(1000):
    tmp_list.append(i)

# ####### 10000 번을 반복해 평균 실행 시간을 내는 코드
time_sum = 0
for idx in range(10000):
    time1 = time.time()

    # 실행시간 테스트할 함수 변경 부분
    count_prime3_1(1000)
    #
    op_time = time.time() - time1
    time_sum += op_time

    print(f"실행시간은 {op_time}입니다. ")
print(f"평균 실행시간은 '{time_sum / 10000}'초 입니다.")

