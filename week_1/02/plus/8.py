# MARK: 문제 8
# 문제8) 사용자로부터 시간(시간과 분)을 입력받아, 해당 시간을 분 단위로 변환하여
# 출력하는 프로그램을 작성하세요.
# <예시>
# 입력: 시간을 입력하세요 (예: 2시간 30분 -> 2 30): 2 30
# 출력: 총 150분입니다.
# - split() 함수를 이용해 시간과 분을 분리.
import re

time = input("시간을 입력하세요 (예: 2시간 30분) : ")
numbers = re.findall(r'\d+', time)

print((int(numbers[0])*60) + int(numbers[1]))


input_time = input("시간을 입력하세요 (예: 2시간 30분 -> 2 30): ")
time_parts = input_time.split()

hours = int(time_parts[0])
minutes = int(time_parts[1])
total_minutes = hours * 60 + minutes

print(total_minutes)
