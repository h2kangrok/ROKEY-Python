# AMRK: 문제 11
# 11.	주어진 문자열을 리스트로 만들고, 리스트 메소드인 sort() 함수를 사용하여 만들어진 리스트를 오름차순으로 정렬한다.
# sort()함수에 매개변수 reverse=True를 설정하여 역순으로 정렬한 리스트를 출력하는 프로그램을 작성하시오.

data = '잣밤배귤감'


def solution(data):
    data_list = [char for char in data]
    data_list.sort()
    data_list.sort(reverse=True)

    return data_list


print(solution(data))
