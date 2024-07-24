# MARK: 문제 6
# 문제6) 인공지능 로봇 "AI-Robo"는 매우 현란한 기능을 가진 최신 모델입니다. 그러나 로봇의 배터리는 일정 시간 이상 작동하지 못할 경우 교체해야 합니다. "AI-Robo"의 배터리는 각 배터리 셀이 독립적으로 관리되며, 각 셀의 잔여 용량이 다를 수 있습니다.
# 로봇에는 현재 사용 중인 5개의 배터리 셀이 있습니다. 각 셀의 잔여 용량(단위: %)이 주어집니다. "AI-Robo"가 최대한 오랫동안 작동하기 위해 가장 낮은 잔여 용량을 가진 배터리 셀 하나를 교체하려고 합니다.

batteryArr = [30, 50, 20, 80, 10]

min_capacity = batteryArr[0]
min_index = 0

for i in range(1, len(batteryArr)):
    if batteryArr[i] < min_capacity:
        min_capacity = batteryArr[i]
        min_index = i

print(f"가장 낮은 잔여 용량을 가진 배터리 셀의 인덱스는 {min_index}입니다.")
