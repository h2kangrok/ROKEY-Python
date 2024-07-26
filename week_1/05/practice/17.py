# 문제17) 섭씨와 화씨온도를 서로 변환시키는 프로그램을 작성한다.

# 섭씨를 화씨로 변환하는 함수
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 화씨를 섭씨로 변환하는 함수


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    print("1: 섭씨를 화씨로 변환")
    print("2: 화씨를 섭씨로 변환")

    choice = input("원하는 변환 옵션을 입력하세요 (1 or 2): ")

    if choice == '1':
        celsius = float(input("섭씨 온도를 입력하세요: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C는 {fahrenheit}°F입니다.")
    elif choice == '2':
        fahrenheit = float(input("화씨 온도를 입력하세요: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F는 {celsius}°C입니다.")
    else:
        print("잘못된 선택입니다.")


main()
