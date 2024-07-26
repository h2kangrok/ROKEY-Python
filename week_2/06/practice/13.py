# 문제13) 세 명의 성적을 입력으로 전달받고, 화면에 순서대로 출력하는 함수를 작성하고, 이 함수를 호출하는 코드를 구현하시오.
# - 일반적으로 성적은 내림차순으로 출력하지만, 가끔씩 반대로 출력하는 경우도 있음. 매개 변수를 이용해서 결정할 수 있도록 할 것
# <요구사항>
# - 매개변수의 기본값을 내림차순으로 지정

def grades(grade1, grade2, grade3, ascending=False):
    grades = [grade1, grade2, grade3]

    sorted_grades = sorted(grades, reverse=not ascending)
    print(*sorted_grades)


print("내림차순 출력")
grades(85, 90, 78)

print("오름차순 출력")
grades(85, 90, 78, ascending=True)
