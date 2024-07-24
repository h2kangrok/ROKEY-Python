# MARK: 문제 8
# 8.	서울시에 살고 있는 구별 인구 중 10개를 가나다순으로 뽑아서 문자열 (guPopulation)을 만들었다. 이 문자열을 이용해서 구:인구 형태의 딕셔너리를 구성하라.
# <요구사항>
# - 사용자는 정수를 입력할 것이라고 가정
# - 만약 사용자가 입력한 정수값(num)보다 작은 구가 없으면 “인구가 num보다 작은 구가 없습니다＂를 출력
# - 구:인구 형태로 출력

guPopulation = "강남구 600000 강동구 400000 강북구 300000 강서구 500000 관악구 450000 광진구 350000 구로구 470000 금천구 350000 노원구 470000 도봉구 420000"

guPopulation_dict = {}


def make_dict(guPopulation):
    guPopulation_list = guPopulation.split()

    # 콜론을 공백으로 수정
    guPopulation = guPopulation.replace(":", " ")
    guPopulation_list = guPopulation.split()

    for i in range(0, len(guPopulation_list) - 1, 2):
        gu = guPopulation_list[i]
        population = int(guPopulation_list[i + 1])
        guPopulation_dict[gu] = population

    n = int(input("정수를 입력하세요: "))
    smaller_gu_found = False

    for gu, population in guPopulation_dict.items():
        if population < n:
            print(f"{gu} : {population}")
            smaller_gu_found = True

    if not smaller_gu_found:
        print(f"인구가 {n}보다 작은 구가 없습니다.")


make_dict(guPopulation)
