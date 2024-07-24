from collections import defaultdict

# 주어진 문자열
text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

# 공백과 구두점 제거하고 소문자로 변환
cleaned_text = text.lower().replace('.', '').replace(',', '')

# 단어를 나누고 알파벳만으로 이루어진 단어를 필터링
words = cleaned_text.split()

# 각 알파벳 별로 시작하는 단어들을 저장할 딕셔너리
alpha_words = defaultdict(set)

# 각 단어를 첫 글자 기준으로 그룹화
for word in words:
    if word.isalpha():  # 알파벳만 포함된 단어인지 확인
        first_char = word[0]
        alpha_words[first_char].add(word)

# 결과 출력
for char in sorted(alpha_words.keys()):
    words_list = sorted(alpha_words[char])
    print(f"{char} : {', '.join(words_list)}")
