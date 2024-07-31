# MARK: 문제 10

# 10.	아래의 문자열(HTML)에서 모든 태그를 찾는 코드를 작성하시오.

import re

text = "<html><head><title>Test</title></head><body><h1>Header</h1><p>Paragraph</p></body></html>"
tags = []
fail_tags = []

pattern1 = r"<[a-zA-Z0-9]+>"
pattern2 = r"</[a-zA-Z0-9]+>"

start_tags = re.findall(pattern1, text)
end_tags = re.findall(pattern2, text)

end_tag_list = [s.replace("/", "") for s in end_tags]

for tag in start_tags:
    if tag in end_tag_list:
        tags.append(tag)
    else:
        fail_tags.append(tag)

if fail_tags:
    print(
        f"문자열에 들어있는 태그는 {','.join(tags)} 제대로 닫히지 않은 태그는 {','.join(fail_tags)}")
else:
    print(f"문자열에 들어있는 태그는 {', '.join(tags)} 입니다.")

# import re

# text = "<html><head><title>Test</title></head><body><h1>Header</h1><p>Paragraph</p></body></html>"

# # 모든 태그를 찾기 위한 정규 표현식
# pattern1 = r'<([a-zA-Z0-9]+)[^>]*>'
# pattern2 = r'</([a-zA-Z0-9]+)>'

# # 시작 태그와 끝 태그 추출
# start_tags = re.findall(pattern1, text)
# end_tags = re.findall(pattern2, text)

# # 시작 태그와 끝 태그를 세트로 변환
# start_tags_set = set(start_tags)
# end_tags_set = set(end_tags)

# # 올바르게 닫힌 태그와 닫히지 않는 태그 분리
# tags = list(start_tags_set & end_tags_set)
# fail_tags = list(start_tags_set - end_tags_set)

# print(f"문자열에 들어있는 태그는 {tags}")

# if fail_tags:
#     print("제대로 닫히지 않는 태그는 다음과 같습니다:")
#     for tag in fail_tags:
#         # 원본 문자열에서 해당 태그와 매칭되는 부분을 찾기
#         pattern_fail_tag = fr'<{tag}[^>]*>|</{tag}>'
#         matches = re.findall(pattern_fail_tag, text)
#         print(f"{tag}: {matches}")
# else:
#     print("모든 태그가 올바르게 닫혀 있습니다.")
