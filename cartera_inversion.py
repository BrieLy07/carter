# Pulp es una biblioteca de optimización de Python que se utiliza para resolver problemas de programación lineal.
from pulp import *

# Datos del problema
# Se establecen los precios actuales, rendimientos esperados y el presupuesto inicial.
precios = {'AAPL': 150, 'GOOGL': 2000, 'AMZN': 3200}
# Se establecen los rendimientos esperados para cada acción.
rendimientos = {'AAPL': 0.15, 'GOOGL': 0.12, 'AMZN': 0.18}
# Se establece el presupuesto inicial para la inversión.
presupuesto = 10000

# Crear el modelo de optimización (problema de maximización)
model = LpProblem("Maximizar_Rendimiento", LpMaximize)

# Crear las variables de decisión
# Se define una variable por cada acción a comprar, con un límite inferior de 0 y tipo entero.
acciones = LpVariable.dicts("Acciones", precios.keys(), lowBound=0, cat='Integer')

# Función objetivo: Maximizar el rendimiento total
# Se multiplica el rendimiento esperado por el precio de cada acción y se suman todas las acciones.
model += lpSum([rendimientos[i] * precios[i] * acciones[i] for i in precios.keys()]), "Rendimiento_Total"

# Restricción de presupuesto
# El costo total de las acciones compradas no debe superar el presupuesto inicial.
model += lpSum([precios[i] * acciones[i] for i in precios.keys()]) <= presupuesto, "Presupuesto"


# Resolver el modelo
# Se resuelve el modelo de optimización y se imprime el estado de la solución.
model.solve()

# Imprimir la solución
# Se imprime el estado de la solución y la composición de la cartera óptima.
# Si es optimo es la mejor solución para las restricciones que hemos colocado, si es infeasible no se puede resolver.
print("Estado:", LpStatus[model.status])
print("Composición de la cartera:")
for v in model.variables():
    if v.varValue > 0:
        print(f"- {v.name}: {v.varValue} acciones")



