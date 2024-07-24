from string import ascii_lowercase

# 주어진 문자열
text = '''The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. 
Professor Kennicot of Palmira University was the first to find how to generate and control them. 
He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.
Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. 
The heaviside layer did not stop these wavelengths.
Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.'''

cleaned_text = text.lower()

used_chars = {char for char in cleaned_text if char.isalpha()}

all_alphabets = set(ascii_lowercase)

missing_alphabets = all_alphabets - used_chars

if missing_alphabets:
    print("나타나지 않은 알파벳:", " ".join(sorted(missing_alphabets)))
else:
    print("나타나지 않은 알파벳은 없습니다.")
