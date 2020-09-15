pessoa1 = input()
pessoa2 = input()

n1, i1 = pessoa1.split()
n2, i2 = pessoa2.split()
i1 = int(i1)
i2 = int(i2)

if i1 > i2:
    print(n1)
elif i2 > i1:
    print(n2)
else:
    print(f'{n1} e {n2} tem a mesma idade')