def number_coroutine():
    while True:
        x = (yield)
        print(x, end=" ")


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)
