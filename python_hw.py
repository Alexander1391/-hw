import math


a = 56
b = 13
c = 100
result = a + b * ( c / 2 )
print("рерультат произвольных значений: a = %f и b = %d и c = %d  равна %f" % (a, b, c, result))


a = 56
b = 13
result = (a**2 + b**2) % 2
print(result)

a = 56
b = 13
c = 100
result = ( a + b ) / 12 * c % 4 + b
print(result)

player1 = 1.36
player2 = 57
player3 = 4
players = (player1 - player2 * player3 ) / ( player1 + player2 ) % player3
print("рерультат произвольных значений: player1 = %f и player2 = %d и player3 = %d  равна %f" % (player1, player2, player3, players))

a = 12
b = 7
c = 30
results = abs(a - b) / (a + b)**3 - math.cos( c )
print(results)


a = 12
b = 7
c = 30
lnt = (math.log( 1 + c ) / -b )**4+ abs(a)
print(lnt)
