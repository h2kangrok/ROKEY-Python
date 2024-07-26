# MARK: 문제 7

# 문제7) 다음 두 print()문에 대한 예외 처리를 구현해 다음과 같은 결과가 나오도록 아래 코드를 완성하시오..
# (1) print(int(“abc”))에 대한 결과
#      예외 발생 이름: <class 'ValueError'>
#      예외 발생 이유: invalid litera; for int( with base 10: ‘abc’)
#      예외 처리가 잘되는군요!

# try:
#     print(int("abc"))
# except ValueError as e:
#     print(f"예외 발생 이름: {type(e)}")
#     print(f"예외 발생 이유: {e}")
# else:
#     pass
# finally:
#     print("예외 처리가 잘되는군요!")

# (2) print(“10”)에 대한 결과
#      12
#      잘 실행됐습니다.
#      예외 처리가 잘되는군요!

# try:
#     print(int("10"))
# except Exception as e:
#     pass
# else:
#     print("잘 실행됐습니다.")
# finally:
#     print("예외 처리가 잘되는군요!")
