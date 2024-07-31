# MARK: 문제 6
# 6.	아래 문자열에 특정 단어(‘sample')가 있는지 확인하는 코드를 작성하시오.
import re

text = "This is a sample text with the word 'sample' in it."

pattern = r"sample"

match = re.search(pattern, text)

if match:
    print("문자열에 sample이 있습니다!")
else:
    print("문자열에 sample이 없습니다!")
