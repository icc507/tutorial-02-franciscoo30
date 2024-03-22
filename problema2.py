#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

t = input().split()

tupla_convertida = tuple(int(x) if x.isdigit() else x for x in t)

tupla_invertida = tupla_convertida[::-1]
print(tupla_invertida)
