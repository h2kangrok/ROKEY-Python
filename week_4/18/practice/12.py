# MARK: 문제 12
# 12.	주어진 텍스트 안의 모든 특수문자를 제거하는 정규표현식을 만들어 보세요.
import re

text = "Hello! @world! This is 2024. @#$%^&*"

pattern = r"[^\w\s]"

clean_text = re.sub(pattern, "", text)

print(clean_text)
