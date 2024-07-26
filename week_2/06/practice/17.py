# 문제17) 아래의 코드를 실행했을 때 어떤 결과가 나오는지 예측해 보세요.
def hello(*names):
    for each in names:  # names 내의 모든 요소들을 순서대로 참조하는 순환문
        print('안녕, {}!'.format(each))


hello('민정')
hello('David', 'Veronica', 'Paul')
hello('방탄소년단', '블랙핑크')


def hello(*names):
    for each in names:  # names 내의 모든 요소들을 순서대로 참조하는 순환문
        print('안녕, {}!'.format(each))


hello('민정')
hello('David', 'Veronica', 'Paul')
hello('방탄소년단', '블랙핑크')
