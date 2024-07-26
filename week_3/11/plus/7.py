# MARK: 문제 7
from collections import defaultdict

# 주어진 문자열
text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

cleaned_text = text.lower().replace('.', '').replace(',', '')

words = cleaned_text.split()

alpha_words = defaultdict(set)


for word in words:
    if word.isalpha():
        first_char = word[0]
        alpha_words[first_char].add(word)

for char in sorted(alpha_words.keys()):
    words_list = sorted(alpha_words[char])
    print(f"{char} : {', '.join(words_list)}")
