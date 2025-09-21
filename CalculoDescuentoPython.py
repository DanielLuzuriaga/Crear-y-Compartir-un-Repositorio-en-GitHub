# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Programa principal
def main():
    # Primera llamada: solo monto total (usará el 10% por defecto)
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    total_a_pagar1 = monto1 - descuento1
    print(f"Compra 1:\nMonto Total: ${monto1:.2f}\nDescuento (10%): ${descuento1:.2f}\nTotal a Pagar: ${total_a_pagar1:.2f}\n")

    # Segunda llamada: monto total + porcentaje de descuento personalizado
    monto2 = 500.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total_a_pagar2 = monto2 - descuento2
    print(f"Compra 2:\nMonto Total: ${monto2:.2f}\nDescuento ({porcentaje2}%): ${descuento2:.2f}\nTotal a Pagar: ${total_a_pagar2:.2f}")

# Ejecutar el programa
main()
