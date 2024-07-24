# MARK: 문제 2
# 2.	각 학생이 듣는 과목을 집합으로 저장한 후 모든 학생이 듣는 과목, 한 명이라도 듣는 과목,
# 한 명씩만 듣는 과목을 구하는 프로그램을 작성하시오.
student_courses = {
    "학생1": {"수학", "과학", "영어"},
    "학생2": {"수학", "음악", "미술"},
    "학생3": {"수학", "과학", "음악"}
}


def analyze_courses():

    all_students_courses = set.intersection(*student_courses.values())
    any_student_courses = set.union(*student_courses.values())

    from collections import Counter
    course_counts = Counter()

    # 각 과목의 출현 횟수를 세기
    for courses in student_courses.values():
        course_counts.update(courses)

    one_time_courses = {course for course,
                        count in course_counts.items() if count == 1}

    print(f"모든 학생이 듣는 과목: {all_students_courses}")
    print(f"한 명이라도 듣는 과목: {any_student_courses}")
    print(f"한 명씩만 듣는 과목: {one_time_courses}")


analyze_courses()
