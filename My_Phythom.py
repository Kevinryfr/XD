numero = int(input("escoje un numero: "))
numero2 = int(input("escoje otro numero: "))
print("¿que quieres hacer?")
print("1 para multiplicar")
print("2 para sumar")
print("3 para restar")
print("4 para dividir")

res = int(input("pon tu respuesta aqui: "))

if res ==1:
    print(f"la multiplicacion es: {numero * numero2}")
elif res ==2:
    print(f"la suma es: {numero + numero2}")
elif res ==3:
    print(f"la resta es: {numero - numero2}")
elif res ==2:
    print(f"la suma es: {numero / numero2}")
else:
    print("opcion invalidad")