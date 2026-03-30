# 2. Diagrama de Clases (Teoría)

### Teoría
Muestra la estructura estática del sistema detallando las clases, sus atributos, métodos y las relaciones entre los objetos. Es el plano directo para la Programación Orientada a Objetos (POO).

### Relaciones y Acoplamiento
* **Dependencia (`..>`):** Acoplamiento muy débil. Una clase "usa" a otra transitoriamente (ej. se pasa como parámetro).
* **Asociación (`-->`):** Acoplamiento moderado. Una clase tiene un atributo del tipo de la otra, pero con ciclos de vida independientes.
* **Agregación (`o--`):** Acoplamiento moderado-fuerte. Relación "Todo-Parte" donde las partes existen independientemente del todo (p. ej. Inyección de dependencias).
* **Composición (`*--`):** Acoplamiento muy fuerte. Relación "Todo-Parte" estricta; si se destruye el contenedor, se destruyen las partes.
* **Herencia / Generalización (`<|--`):** Acoplamiento extremo. Relación "Es un" (Is-A).
* **Realización / Implementación (`<|..`):** Implementación de una interfaz.
