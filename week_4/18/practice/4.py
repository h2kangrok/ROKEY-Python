# MARK: 문제 4
# 4.	아래 문자열 안에 이메일 주소들이 들어 있습니다.
# 정규표현식(Regex)을 이용해 이메일 주소를 찾는 코드를 작성하시오.

# text = "alice@example.com 이 첫 번째 이메일이고, 다음은 bob.smith@mail.co.uk 입니다."

import re

text = "alice@example.com 이 첫 번째 이메일이고, 다음은 bob.smith@mail.co.uk 입니다."

# 일반 문자열로 이메일 패턴을 정의
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# match 메소드를 이용해 문자열의 시작에서 패턴에 매칭되는지 확인
# Write your code here
match = re.match(pattern, text)

if match:
    print(match.group())
else:
    print("문자열의 시작 부분에 이메일이 없습니다.")
