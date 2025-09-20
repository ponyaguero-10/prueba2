# Lista de números
numeros = [2, 5, 6, 8, 9]

# Pedir número al usuario
valor = int(input("Ingresa un número: "))

# Verificar si está en la lista
if valor in numeros:
    print("✅ Número encontrado en la lista.")
else:
    print("❌ Número NO encontrado en la lista.")