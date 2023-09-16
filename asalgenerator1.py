"""
def asal(sayi):
    i = 2
    while i <sayi:
        if sayi % i == 0:
            return False
        i +=1
    return True



def asalgen():
    i =2
    while True:
        if (asal(i)):
            yield i
        i += 1

for i in asalgen():
    if i > 1000:
        break
    print(i)
    """



def asal(sayi):
    i = 2
    while i < sayi:
        if sayi %i == 0:
            return False
        i+=1
    return True


def generator():
    i = 2
    while True:
        if (asal(i)):
            yield i
        i+=1
        if i > 1000:
            break
a =asal(1000)
for i in generator():
    print(i)