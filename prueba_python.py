producto = "Servicio de edición de vídeo"
precio = 25
clientes = 4

ingresos = precio * clientes

print("Servicio:", producto)
print("Ingresos totales:", ingresos, "euros")

if ingresos >= 100:
    print("Objetivo alcanzado")
else:
    print("Todavía no alcanzamos el objetivo")
    clientes = ["Juan", "Pedro", "María"]

for cliente in range(clientes):
    print("Cliente número:", cliente + 1)
    print("Preparar presupuesto para:", cliente)
lista_clientes = ["Juan", "Pedro", "María"]

for cliente in lista_clientes:
    print("Preparar presupuesto para:", cliente)
    print("OBJETIVO: CONSEGUIR 5 CLIENTES")

clientes_conseguidos = 0

while clientes_conseguidos < 5:
    clientes_conseguidos += 1
    print("Nuevo cliente conseguido:", clientes_conseguidos)

print("¡Objetivo de 5 clientes alcanzado!")
clientes_actuales = 5

while clientes_actuales < 10:
    clientes_actuales += 1
    print("Clientes conseguidos:", clientes_actuales)

print("¡Objetivo de 10 clientes alcanzado!")
