def calcularIVA(importe):
    importe = int(input(f"Precio del producto: {importe}"))
    total = importe * 1.21
    print(f"IVA incluido (21%): {total}")
    return

print("Llamamos a la funcion")
calcularIVA()