# MARK: 문제 9
# 문제9) 아래의 파일의 인코딩 방식을 'utf-8'로 설정하도록 코드를 수정하시오.

with open("python.utf8.txt", "r", encoding="utf-8") as f:
    s = f.read()
    print(s)
