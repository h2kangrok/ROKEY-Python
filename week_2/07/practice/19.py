# 문제19) 다음의 복리 계산 방식을 사용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# - 1년: 복리총액 1,024,265월, 총이자액 24,265원
# - 입력데이타: 원금, 연이자율, 투자기간(년)

def calculate_compound_interest(principal, annual_interest_rate, investment_period):
    total_amount = principal * \
        (1 + annual_interest_rate / 100) ** investment_period
    total_interest = total_amount - principal

    return total_amount, total_interest


principal = int(input("원금을 입력하세요 (원): "))
annual_interest_rate = float(input("연이자율을 입력하세요 (%): "))
investment_period = int(input("투자기간을 입력하세요 (년): "))

total_amount, total_interest = calculate_compound_interest(
    principal, annual_interest_rate, investment_period)
print(f"{investment_period}년: 복리총액 {total_amount:,.0f}원, 총이자액 {total_interest:,.0f}원")
