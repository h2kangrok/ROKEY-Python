# MARK: 문제 7

# 7.	클래스 Car에서 다음 조건의 매직 메소드를 만들어 아래와 같은 결과가 나오도록 프로그램을 작성하라.
# - 초기화 메소드 __init__
# - 문자열화 메소드 __str__
# - 동등 비교 메소드 __eq__: 객체의 모든 값이 동일하면 True, 아니면 False를 반환


class Car:
    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color

    def __str__(self):
        return f"자동차 회사 : {self.company}, 년식 : {self.year},  색상 : {self.color}"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (self.company == other.company and
                self.year == other.year and
                self.color == other.color)


# 예시 코드
mycar = Car('ABC', 2020, '검정')
yourcar = Car('DEF', 2021, '백색')
print(mycar)
print(yourcar)
print(mycar == yourcar)
