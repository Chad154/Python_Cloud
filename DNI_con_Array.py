cadena = int(input("Introduzca su número de DNI sin letra: "))

# Lista de letras correspondientes
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

# Calcular la letra
letra = letras[cadena % 23]

# Imprimir resultado
print(cadena, letra)
