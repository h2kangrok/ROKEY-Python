# MARK: 문제 5
from collections import Counter

# 주어진 문자열
text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

text = text.replace(" ", "")

char_counter = Counter(text)

most_common_chars = char_counter.most_common()


if len(most_common_chars) > 1:
    second_most_common = most_common_chars[1]
    print(
        f"두 번째로 많이 나타난 문자: '{second_most_common[0]}' ({second_most_common[1]}회)")
