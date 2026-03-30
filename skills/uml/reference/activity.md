# 4. Diagrama de Actividades (Teoría)

### Teoría
Modela el flujo de control de un proceso o caso de uso, soportando ejecución paralela y concurrente. Las "calles" (swimlanes) ayudan a definir responsables o componentes involucrados en cada paso.

### Relaciones
* **Transición (`-->`):** Orden secuencial básico.
* **Bifurcación (`if / else / endif`):** Caminos excluyentes según reglas de negocio.
* **Sincronización (`fork / fork again / end fork`):** Múltiples flujos que corren en paralelo e independientes.
