# MARK: 문제 9
# 9.	아래의 문자열에 있는 모든 소수점을 포함한 숫자를 찾는 코드를 작성하시오.

import re

text = "상품의 가격은 19.99달러와 100.0달러, 0.99달러 입니다."

pattern = r"[0-9]+\.[0-9]+"

match = re.findall(pattern, text)

if match:
    print(f"문자열에 있는 모든 소수점을 포함한 숫자 : {match}")
else:
    print("문자열에 존재하지 않습니다.")
