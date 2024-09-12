numeros = [0,1,2,3,4,5]

print("-------")
for numero in numeros:
    print(numero)

print("-------")
for x in range(5):
    print(x)

print("-------")
for y in range(2,7):
    print(y)

print("-------")
#Min, max, incremento
for z in range(2,10,2):
    print(z)

print("-------")
for n in range(1,11):
    if n %2 == 0:
        print(n)
        #Para no primeiro resultado
        break

print("-------")
for r in range(1,11):
    if r == 5:
        #Pula
        continue
    print(r)