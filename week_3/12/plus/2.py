# MARK: 문제 2
# 2.	아래 코드를 실행하여 출력 결과를 확인하고, 그 결과가 나온 이유를 서술하시오(결과가 나온 이유만 작성하셔도 됩니다).

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle initialized: {self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        car = Vehicle("AAA", "BBB")  # 부모 클래스의 생성자 호출
        self.horsepower = horsepower
        print(
            f"Car initialized: {self.brand} {self.model} with {self.horsepower} HP")


# 객체 생성
my_car = Car("AAA", "BBB", 350)


# 부모 클래스 (Vehicle): 이 클래스는 모든 차량의 기본 정보인 브랜드와 모델을 초기화합니다.
# 생성자 메서드 __init__에서 이 두 속성을 설정합니다.

# 자식 클래스 (Car): 이 클래스는 Vehicle을 상속받아 더 구체적인 차량 유형인 'Car'를 표현합니다.
# 추가로 horsepower 속성이 포함됩니다. 자식 클래스의 생성자에서 super().__init__(brand, model)을 호출함으로써,
# 부모 클래스의 생성자를 실행하고 브랜드와 모델을 초기화합니다.
# 이렇게 하면 Car 인스턴스를 생성할 때 Vehicle의 모든 초기화 로직을 재사용할 수 있습니다.
