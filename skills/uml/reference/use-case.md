# 1. Diagrama de Casos de Uso (Teoría)

### Teoría
Los diagramas de casos de uso describen el comportamiento del sistema desde el punto de vista del usuario (o "actor"). No se centran en cómo se hace algo a nivel técnico, sino en qué hace el sistema. Son fundamentales para la recolección de requisitos y para definir los límites del sistema.

### Tipos de Relaciones y Cuándo Usarlas
* **Asociación (Comunicación) (`--`):** Conecta a un actor con un caso de uso en el que participa. Usar cuando un usuario interactúa directamente con una función del sistema.
* **Inclusión (`..> : <<include>>`):** Un caso de uso base incorpora explícitamente el comportamiento de otro caso de uso. Útil para evitar duplicar código/pasos obligatorios.
* **Extensión (`..> : <<extend>>`):** Un caso de uso añade comportamiento a un caso de uso base, solo bajo ciertas condiciones (comportamientos opcionales).
* **Generalización (Herencia) (`-!>`):** Un actor o caso de uso hereda de otro más general.
