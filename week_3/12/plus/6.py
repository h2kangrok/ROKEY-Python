# MARK: 문제 6
# 6.	아래 자료(딕셔너리)는 연도별 고등학교의 학급당 학생 수이다(출처: 2021 교육 기본 통계 결과 발표 자료) 아래의 요구사항을 프로그램으로 작성하라.
# d = {2010:33.7, 2011:33.1, 2012:32.5, 2013:31.9, 2014:30.9, 2015:30.0, 2016:29.3, 2017:28.2, 2018:26.2, 2019:24.5, 2020:23.4, 2021:23} #년도:학급당 학생수
# 요구사항
# 1. 전해에 비해 가장 급격하게 학생 수가 줄어든 해는 언제인가?
# 2. 학급당 학생 수가 30명 미만으로 떨어진 해는 언제인가?
# 3. 2010년부터 2021년 사이에 평균적으로 학급당 학생 수는 어느 정도 감소했는가?

class Problem:
    def __init__(self, studentsNumDictionary):
        self.studentsNumDictionary = studentsNumDictionary

    def subproblem1(self):
        max_decrease = 0
        year = 0
        prev_year = None

        # Use the sorted keys of the dictionary to find the maximum decrease
        for current_year in sorted(self.studentsNumDictionary.keys()):
            if prev_year is not None:
                decrease = self.studentsNumDictionary[prev_year] - \
                    self.studentsNumDictionary[current_year]
                if decrease > max_decrease:
                    max_decrease = decrease
                    year = current_year
            prev_year = current_year

        print(f"(1) {year}에 {max_decrease:.1f}명 감소한 것이 최근 가장 급격하게 줄어든 경우입니다.")

    def subproblem2(self):
        # Find the first year when the number of students per class drops below 30
        for year in sorted(self.studentsNumDictionary.keys()):
            if self.studentsNumDictionary[year] < 30:
                print(f"(2) 학생 수가 30명 미만으로 떨어진 첫 해는 {year}년입니다.")
                break

    def subproblem3(self):
        # Calculate the average decrease in number of students per class from 2010 to 2021
        years = sorted(self.studentsNumDictionary.keys())
        total_decrease = self.studentsNumDictionary[years[0]
                                                    ] - self.studentsNumDictionary[years[-1]]
        average_decrease = total_decrease / (len(years) - 1)

        print(f"(3) 2010년부터 2021년까지 평균적으로 감소한 학생 수는 {average_decrease:.2f}명이다")


d = {2010: 33.7, 2011: 33.1, 2012: 32.5, 2013: 31.9, 2014: 30.9, 2015: 30.0,
     2016: 29.3, 2017: 28.2, 2018: 26.2, 2019: 24.5, 2020: 23.4, 2021: 23}

p = Problem(d)
p.subproblem1()
p.subproblem2()
p.subproblem3()
