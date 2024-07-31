# MARK: 문제 2

# 2.	다음 코드가 어떤 작업을 하는지 생각해 보고 결과를 확인 하시오.


import re  # 정규표현식을 사용하여 문자열 검색, 매칭, 치환 등의 작업을 수행할 수
# 있게 해주는 모듈
# 테스트할 문장 목록
sentences = ["I love programming in Python.",
             "JavaScript is a versatile language.",
             "The Python snake is a non-venomous species."]

# 정규표현식 패턴
pattern = r'Python'

# 문장 판별
for sentence in sentences:
    if re.search(pattern, sentence):
        print(f"'Python' found in: \"{sentence}\"")
    else:
        print(f"'Python' not found in: \"{sentence}\"")
