# MARK: 문제 15
# 문제 15


seat_type = input("구매할 좌석의 종류를 입력하세요. : ")

if seat_type == 'VIP':
    print(f"VIP 좌석의 가격은 150000원입니다.")
elif seat_type == "S":
    print(f"S 좌석의 가격은 110000원입니다.")
elif seat_type == "A":
    print(f"A 좌석의 가격은 90000원입니다.")
elif seat_type == "B":
    print(f"B 좌석의 가격은 70000원입니다.")
else:
    print("잘못된 입력입니다.")
