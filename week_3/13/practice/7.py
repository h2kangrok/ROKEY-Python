# MARK: 문제 7

# 7.	time_utils.py라는 모듈을 만드세요. 이 모듈에는 시간과 관련된 여러 유틸리티 함수를 포함합니다.
# - current_time(): 현재 시간을 반환합니다.(형식은 “2024-07-01 01:23:07”과 같아야 합니다.)
# - sleep_for(seconds): 주어진 초만큼 일시 정지합니다.
# - time_elapsed(start_time): 주어진 시작 시간부터 경과된 시간을 반환합니다.

import time_utils
import time

print("Current time:", time_utils.current_time())  # a
print("Sleeping for 2 seconds...")
start_time = time.time()
time_utils.sleep_for(2)  # b
print("Current time:", time_utils.current_time())  # c
print("Elapsed time after sleeping:",
      time_utils.time_elapsed(start_time), "seconds")
