# 문제7) 위 문제를 하나의 함수 getSum()을 작성해서 해결해 보세요.
# 코드의 중복없이 하나의 함수를 공통으로 사용하기 위해서 필요한 입력과 출력을 설계하세요.

def getSum(start, end, type):
    i = start
    total_sum = 0
    while i <= end:
        if type == "sum":
            total_sum += i
        elif type == "even_sum":
            if i % 2 == 0:
                total_sum += i
        elif type == "factor_of_3":
            if i % 3 == 0:
                total_sum += i
        i += 1
    return total_sum


print(f"100 ~ 199까지의 합계를 계산: {getSum(100, 199, 'sum')}")
print(f"100 ~ 199까지의 짝수의 합계를 계산: {getSum(100, 199, 'even_sum')}")
print(f"100 ~ 199까지의 3의 약수만 합계를 계산: {getSum(100, 199, 'factor_of_3')}")
