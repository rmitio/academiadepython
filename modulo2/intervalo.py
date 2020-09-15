n = int(input())
if n >= 0 and n <= 50:
    print('[0, 50]')
elif n >= 51 and n <= 100:
    print('[51, 100]')
else:
    print('Fora do intervalo')