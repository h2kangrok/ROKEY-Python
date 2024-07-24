# MARK: 문제 3
# 3.	다음 문장은 Robert Zaks라는 사람이 쓴 "From Outer Space"라는 SF소설에서 일부 발췌한 내용이다. 해당 내용은 저작권이 만료된 자료로 전문은 구텐베르크 프로젝트 사이트 (링크)에서 구할 수 있다.
# 해당 내용을 단어 단위로 잘라서 각 단어들이 몇회 나타나는지 기록하고, 가장 많이 반복된 단어와 두 번째로 많이 반복된 단어를 화면에 출력하는 프로그램을 작성한다.
# The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
# Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.
# Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
# 이 내용을 단어로 잘라서 각 단어들이 몇 회 나타나는지 기록하고, 가장 많이 반복된 단어와 두 번째로 많이 반복된 단어를 화면에 출력하는 프로그램을 작성한다.
# - 특수 문자는 무시하기로 한다. 문자열의 split() 함수를 사용하면 마침표는 무시하 지만, 콤마(',') 같은 특수 문자는 단어의 일부로 포함될 수 있다. 따라서 단어를 자를 때 콤마를 제거해야 한다.
# - 많이 나타난 빈도수가 중복되는 단어들이 있을 수 있다. 이 경우에는 그 중 한 개를 출력한다.

from collections import Counter
import re

# 주어진 문자열
text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

cleaned_text = re.sub(r"[,.-]", "", text).lower()

# 단어를 나누고 알파벳만으로 이루어진 단어를 필터링
words = cleaned_text.split()
alpha_words = [word for word in words if word.isalpha()]

counter_word = Counter(alpha_words)


most_common = counter_word.most_common(2)
print(most_common)

if len(most_common) > 0:
    print(f"가장 많이 나타난 단어: {most_common[0][0]} ({most_common[0][1]}회)")
if len(most_common) > 1:
    print(f"두 번째로 많이 나타난 단어: {most_common[1][0]} ({most_common[1][1]}회)")
