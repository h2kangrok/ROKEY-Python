# MARK: 문제 5
# 문제5) 원금을 복리로 계산하는 코드를 아래의 공식을 참조하여 작성하시오.

principal = float(input("원금을 입력하세요: "))
annual_interest_rate = float(input("연 이자율(%)을 입력하세요: "))
period = float(input("기간(년수)을 입력하세요: "))  #

monthly_interest_rate = (annual_interest_rate / 100) / 12
amount = principal * (1 + monthly_interest_rate) ** (period * 12)

print(f"복리 계산 결과: {amount}원")
