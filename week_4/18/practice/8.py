# MARK: 문제 8

# 8.	아래의 문자열에 있는 모든 이메일 주소를 raw 문자열 패턴을 사용하여 찾는 코드를 작성해 보시오.
# charlie123@domain.org."

# 이메일 형식은 아래와 같다.
# -	이메일은 영문자, 숫자, @, 마침표로만 구성되어 있다.
# -	이메일은 @와 마침표를 구분자로 사용하여 크게 3부분으로 구성되어 있다.

import re

text = "다음 사람들에게 이메일을 보내세요: alice@example.com, bob.smith@mail.co.uk, charlie123@domain.org."

pattern = r"[0-9a-zA-Z.]+@[0-9a-zA-Z.]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)

print(emails)
