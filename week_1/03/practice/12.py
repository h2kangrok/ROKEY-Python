# MARK: 문제 12
# 문제 12)

import math

b = 17.62
c = 243.12
temperature = 25
humidity = 60

gamma = (b * temperature / (c + temperature)) + math.log(humidity / 100.0)
dewpoint = (c * gamma) / (b - gamma)

print(dewpoint)
