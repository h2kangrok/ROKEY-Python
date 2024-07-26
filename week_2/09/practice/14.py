# 문제14) 강의자료 실습문제 2 에서 파일에서 검색할 문자열을 찾으면, 검색 결과를 새로운 파일에 저장한다.
# 결과를 저장할 파일 이름은 사용자로부터 입력 받는다. 만약 파일에 검색할 문자열이 없으면,
# 화면에 "검색 단어가 파일에 없습니다"라는 메시지만 출력하고 파일은 생성하지 않는다.
# - 검색할 문자열이 없는 경우, 파일을 생성하지 않는다. 그러나 문자열이 있는지 확인하려면 파일 전체를 검색해야 한다.
# 전체를 검색한 후 저장할 내용이 없으면 파일을 생성하지 않는다.
# - 파일 내용을 전체 검색하면서 검색할 단어가 있으면, 이를 우선 리스트에 저장한다.
# 그런 다음 리스트의 크기가 1 이상이면 파일을 열고 검색된 내용을 저장한다.

# 검색할 문자열 -> 검색 결과 새로운 파일에 저장

# 결과를 저장할 파일 이름은 사용자로 부터 입력 받음

# def solution(search_str):
#     with open("new.txt", "r", encoding="utf-8") as f:
#         search_list = [line.strip() for line in f]
#         if search_str in search_list:
#             return True
#         else:
#             return False


# def main():
#     result_list = []

#     while True:
#         try:
#             result_file_name = input("결과를 저장할 파일 이름을 입력하세요. : ")
#             search_str = input("검색할 문자열을 입력하세요. : ")


#             if solution(search_str):
#                 result_list.append(search_str)
#             else:
#                 print("검색 단어가 파일에 없습니다.")
#                 break
#             if len(result_list) >= 1:


#         except ValueError:
#             print("잘못된 입력입니다. ")


# def search_in_file(file_name, search_str):
#     search_results = []
#     try:
#         with open(file_name, "r", encoding="utf-8") as f:
#             lines = f.readlines()
#             for line in lines:
#                 if search_str in line:
#                     search_results.append(line.strip())
#     except FileNotFoundError:
#         print(f"파일 {file_name}을(를) 찾을 수 없습니다.")
#     except Exception as e:
#         print(f"파일을 읽는 동안 오류가 발생했습니다: {e}")
#     return search_results


# def main():
#     file_name = input("검색할 파일 이름을 입력하세요: ")
#     search_str = input("검색할 문자열을 입력하세요: ")
#     result_file_name = input("결과를 저장할 파일 이름을 입력하세요: ")

#     result_list = search_in_file(file_name, search_str)

#     if result_list:

#         try:
#             with open(result_file_name, "w", encoding="utf-8") as result_file:
#                 for result in result_list:
#                     result_file.write(result + "\n")
#             print(f"검색 결과가 {result_file_name} 파일에 저장되었습니다.")
#         except Exception as e:
#             print(f"결과 파일을 쓰는 동안 오류가 발생했습니다: {e}")
#     else:
#         print("검색 단어가 파일에 없습니다.")


# # 프로그램 실행
# main()
