# MARK: 문제 6

# 6.	정해진 기준(1970년 1월 1일 00:00:00 UTC)이후 현재까지 몇 초가 흘렀는지 출력하는 코드를 작성하세요.

import time

current_time = time.time()

print(f"1970년 1월 1일 00:00:00 UTC 이후 현재까지 흘렀던 초: {int(current_time)}")
