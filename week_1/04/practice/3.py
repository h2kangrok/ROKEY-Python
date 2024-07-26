# MARK: 문제 3
# 문제3) 온도 25도 이상, 습도 70이상이면 "에어컨을 켠다" 메시지를 출력하는 코드를 작성한다. 중첩 if문으로작성하고,
# 들여쓰기에 주의한다.

temperature = 36
humidity = 80

if temperature >= 25:
    if humidity >= 70:
        print("에어컨을 켠다")
