def fibo():
    a = 1
    b = 1
    yield b
    yield a
    while True:
        a,b = b, a+b
        yield(b)
        
for i in fibo():
    if i > 100000:
            break
    print(i)


def a():
     a = 1
    
     while True:
          yield a
          a += 1
          if a >=10:
               break
for i in a():
     print(i)
    