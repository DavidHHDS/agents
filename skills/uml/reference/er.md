# 6. Diagrama Entidad-Relación (Teoría)

### Teoría
Mapea la estructura relacional de la base de datos (tablas, columnas) a través de "Crow's Foot" (Pata de gallo) en PlantUML.

### Multiplicidad (Cardinalidad)
* **Uno a Uno (`||--||`):** Relación biunívoca entre dos entidades.
* **Uno a Muchos (`||--o{` o `||--|{`):** Un registro padre puede tener uno o muchos hijos.
* **Muchos a Muchos (`}o--o{`):** Debe resolverse lógicamente con tablas intermedias de resolución.
