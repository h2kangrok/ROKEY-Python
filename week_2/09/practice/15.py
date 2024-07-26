# MARK: 문제 15

# 문제15) data1.txt와 data2.txt에 각각 오름차순으로 정렬된 실수값들이 한 줄에 한 개씩 저장되어 있다.
# 두 개 파일의 데이터를 읽고 오름차순으로 정렬해서 "data3.txt" 파일에 저장하는 프로그램을 작성한다
#  (data1.txt와 data2.txt는 직접 만든다)


def solution():

    with open("data1.txt", "w") as f:
        f.write("0.1\n0.2\n0.3\n0.4\n0.5")
    with open("data2.txt", "w") as f:
        f.write("0.13\n0.24\n0.35\n0.46\n0.57")

    with open("data1.txt", "r")as f1, open("data2.txt", "r") as f2:
        data1 = [float(line.strip()) for line in f1.readlines()]
        data2 = [float(line.strip()) for line in f2.readlines()]
        sorted_data = sorted(data1 + data2)

    with open("data3.txt", "w") as f:
        for number in sorted_data:
            f.write(f"{number} ")

    # data3.txt 파일 읽어서 출력
    with open("data3.txt", "r") as f:
        print(f"data3.txt 데이터 -> {f.read()}")

    print("두 개 파일의 데이터를 읽고 오름차순으로 정렬해서 \"data3.txt\" 파일에 저장이 완료되었습니다! ")


solution()
