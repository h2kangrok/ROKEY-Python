# 문제20) 가위(scissors), 바위(rock), 보(paper) 게임을, 아래의 업무흐름도를 참조해 프로그램을 작성하시오.

p1 = input("scissors, rock, paper 중 하나를 입력하세요. : ")
p2 = input("scissors, rock, paper 중 하나를 입력하세요. : ")


def game(p1, p2):
    if p1 == "rock":
        if p2 == "rock":
            return "비겼습니다."
        elif p2 == "paper":
            return "p2가 이겼습니다."
        elif p2 == "scissors":
            return "p1이 이겼습니다."
        else:
            return "잘못된 입력입니다."
    elif p1 == "paper":
        if p2 == "rock":
            return "p1이 이겼습니다."
        elif p2 == "paper":
            return "비겼습니다."
        elif p2 == "scissors":
            return "p2가 이겼습니다."
        else:
            return "잘못된 입력입니다."
    elif p1 == "scissors":
        if p2 == "rock":
            return "p2가 이겼습니다."
        elif p2 == "paper":
            return "p1이 이겼습니다."
        elif p2 == "scissors":
            return "비겼습니다."
        else:
            return "잘못된 입력입니다."
    else:
        return "잘못된입력입니다."


print(game(p1, p2))


def game(p1, p2):
    if p1 == p2:
        return "비겼습니다."

    if (p1 == "rock" and p2 == "scissors") or \
       (p1 == "scissors" and p2 == "paper") or \
       (p1 == "paper" and p2 == "rock"):
        return "p1이 이겼습니다."

    if (p2 == "rock" and p1 == "scissors") or \
       (p2 == "scissors" and p1 == "paper") or \
       (p2 == "paper" and p1 == "rock"):
        return "p2가 이겼습니다."

    return "잘못된 입력입니다."


def main():

    p1 = input("scissors, rock, paper 중 하나를 입력하세요: ")
    p2 = input("scissors, rock, paper 중 하나를 입력하세요: ")

    valid_choices = {"rock", "paper", "scissors"}

    if p1 not in valid_choices or p2 not in valid_choices:
        print("잘못된 입력입니다. scissors, rock, paper 중에서 선택하세요.")
        return

    print(game(p1, p2))


main()
