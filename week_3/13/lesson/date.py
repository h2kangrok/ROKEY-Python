# from datetime import date
# d = date.today()
# print(d)
# print(d.weekday())

import glob
import sys
lst = []  # 파일 목록
if len(sys.argv) == 1:  # 파이썬 코드만 있음
    lst = glob.glob("*")
else:
    lst = glob.glob(sys.argv[1])
if len(lst) == 0:  # 빈 리스트
    print("매칭되는 파일이 없습니다")
else:
    for name in lst:
        print(name)
