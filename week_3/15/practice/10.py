# MARk: 문제 10

# 10.	산포그래프(Scatter plot)는 데이터 포인트를 점으로 표시하여 두 변수간의 관계를 시각화하는 그래프입니다.
# 주로 두 변수 간의 상관관계, 군집성, 이상치 등을 시각적으로 분석할 때 사용됩니다.
# 주로 matplotlib 와 seaborn 라이브러리를 사용하여 산포그래프를 그려라.


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 주어진 데이터
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 데이터 프레임 생성
data = pd.DataFrame({'x': x, 'y': y})

# 산포그래프 그리기
sns.scatterplot(data=data, x='x', y='y')

# 그래프 제목과 축 라벨 설정
plt.title("Scatter Plot of x and y")
plt.xlabel("x values")
plt.ylabel("y values")

# 그래프 표시
plt.show()
