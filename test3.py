import time

def prime_cnt3(num) -> list:
    cnt = 0
    primes = [2, 3]
    # (정보) 루트 n보다 작은 소수들로 n을 나눴을 때, 모두 나눠 떨어지지 않으면 n은 소수다
    for q in range(5, num + 1, 2):
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
    print(f"입력한 숫자 내에서 소수의 개수는 : {len(primes)}입니다. ")
    return primes

cnt = 0
time_sum = 0
for i in range(10):
    tmptime = time.time()
    # 소수 알고리즘 넣는 곳
    prime_cnt3(3000)
    time_sum += time.time() - tmptime
    cnt += 1
    print(f"{cnt}회 실행 시간은 : {time.time() - tmptime}입니다. ")
print(f"평균 실행 시간은 : {time_sum / cnt }입니다.")

'''2
sum1 = 0
sum2 = 0

## 왜인지 모르겠지만, i ** 2보다 q * q가 약 2배 빠르다
time1 = time.time()
for i in range(10000):
    sum1 += i ** 2
print(f"time1 = {time.time() - time1}, sum1 = {sum1}")

time2 = time.time()
for q in range(10000):
    sum2 += q * q
print(f"time2 = {time.time() -time2}, sum2 = {sum2}")

# '''