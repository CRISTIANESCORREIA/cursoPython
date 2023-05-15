n1 = int(input("digite primeiro numero:"))
n2 = int(input("digite segundo numero:"))
s = n1 + n2
di = n1 / n2
mu = n1 * n2
e = n1 ** n2

print('a soma é {} , \n o produto é {} \n e a divisao é {:.3f}'.format(s, di, mu), end='\n')
print('Divisao inteira {} e potencia {}'.format(di,e))

