a = 0
b =1
fib = [a,b]
for x in range(8):
    a = b
    b = a+b
    fib.append(b)
print(fib)