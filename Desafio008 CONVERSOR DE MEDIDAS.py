#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor= float(input('Uma distância em metros: '))
print ('A medida de {:.1f}m corresponde a:'.format(valor))
print ('{:.3f}km'.format(valor/1000))
print ('{:.2f}hm'.format(valor/100))
print ('{:.1f}dam'.format(valor/10))
print ('{:.0f}dm'.format(valor*10))
print ('{:.0f}cm'.format(valor*100))
print ('{:.0f}mm'.format(valor*1000))