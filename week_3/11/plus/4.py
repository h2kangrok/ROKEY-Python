# MARK: 문제 4
# 4.	3번 문제의 문자열에서 가장 많이 나타난 알파벳 문자와 나타난 횟수를 화면에 출력하는 프로그램을 작성한다.
# - 특수 문자는 무시한다.
# - 공백을 포함해서 특수 문자는 무시하기로 한다.
# - 많이 나타난 빈도수가 중복되는 단어들이 있을 수 있다. 이 경우에는 그 중 한 개를 출력한다.

from collections import Counter
import re

text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

cleaned_text = re.sub(r"[,.-]", "", text).lower()

words = cleaned_text.split()
alpha_words = [word for word in words if word.isalpha()]

counter_word = Counter(alpha_words)
most_common = counter_word.most_common(1)

print(f"가장 많이 나타난 단어: {most_common[0][0]} ({most_common[0][1]}회)")
