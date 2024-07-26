# MARK: 문제 9
# 문제9) 근로 시급이 12,000원이고, 일주일에 40시간 이상 근무하면 시급의 1.5배의 급여를 준다고 한다.
# 근로시간에 따라 주급을 계산하는 프로그램을 작성하시오.

hourly_wage = 12000

working_hours = float(input("근무시간을 입력하세요: "))

if working_hours > 40:
    regular_hours = 40
    overtime_hours = working_hours - regular_hours

    weekly_wage = (regular_hours * hourly_wage) + \
        (overtime_hours * hourly_wage * 1.5)
else:
    weekly_wage = working_hours * hourly_wage

print(f"주급은 : {weekly_wage:.0f}원")

weight = float(input("우편물의 무게를 입력하세요. :"))

if weight <= 5:
    print(f"우편요금 : 400")
elif 5 < weight <= 25:
    print(f"우편요금 : 430")
elif 25 < weight <= 50:
    print(f"우편요금 : 450")
else:
    print("우체국에 문의하십시오.")
