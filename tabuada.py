numero = int(input("Digite um numero para criar a Tabuada: " ))

while (numero < 0 or numero > 10):
        print("VALOR INVÁLIDO") 
        numero = int(input())
if (numero >= 0 or numero <= 10):
    for count in range (10):
        print("%dx%d=%d" % (numero, count+1, numero*(count+1)))