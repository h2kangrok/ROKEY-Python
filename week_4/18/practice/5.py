# MARK: 문제 5

# 5.	아래 문자열이 특정 단어('Hello')로 시작하는지 확인하는 코드를 작성하시오.

import re

text = "Hello, how are you today? Hello, I'm fine."
# 일반 문자열로 'Hello'로 시작하는지 확인하는 패턴 정의
pattern = r"Hello"

# match 메소드를 이용해 문자열의 시작에서 패턴에 매칭되는지 확인
# Write your code here

match = re.match(pattern, text)

if match:
    print("문자열은 'Hello'로 시작합니다.")
else:
    print("문자열은 'Hello'로 시작하지 않습니다.")
