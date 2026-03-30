# Reglas generales de distribucion y espaciado para PlantUML

## 1. Orden de trabajo

1. Define el flujo principal del diagrama: jerarquia, dependencias o secuencia.
2. Agrupa por paquetes o modulos.
3. Ajusta separacion entre clases y relaciones.
4. Agrega notas al final, una por una.
5. Renderiza y valida en SVG.

La razon es simple: las notas son lo mas inestable del layout. Si se agregan demasiado pronto, PlantUML reordena el diagrama varias veces y cuesta detectar la causa real del problema.

## 2. Distribucion general

- Coloca abstracciones o nodos mas estables arriba o en el centro.
- Deja implementaciones concretas abajo o hacia los bordes.
- Mantiene dependencias laterales cuando sea posible y herencias en sentido vertical.
- Usa paquetes con nombres legibles pero compactos. Si un label muy largo abre demasiado el diagrama, acortalo o usa una ruta mas plana.

## 3. Reglas para notas

Para cada nota, evalua esta secuencia:

1. `arriba`: si hay espacio vertical y la nota no cruza una herencia o dependencia importante.
2. `izquierda`: si la clase esta hacia el centro o la derecha y hay una zona libre clara.
3. `abajo`: si la clase esta arriba y no empuja innecesariamente las implementaciones hacia abajo.
4. `derecha`: si la clase esta en el borde izquierdo o el lateral derecho esta libre.

El criterio no es solo que "quepa", sino que la asociacion visual sea corta y obvia.

### Senales de mala ubicacion

- La nota obliga a seguir una linea larga para saber de que clase sale.
- La nota provoca que dos paquetes se separen demasiado.
- La nota genera mucho ancho en el SVG aunque el texto sea corto.
- La nota cruza o roza relaciones importantes.

### Acciones correctivas

- Acortar el texto de la nota antes de aumentar espaciados.
- Cambiar el lado de la nota.
- Quitar la nota de ese diagrama y mover la idea a otro diagrama mas especifico.
- Fusionar dos notas cercanas si explican el mismo bloque conceptual.

## 4. Espaciado base recomendado

Usa estos valores como punto de partida:

```plantuml
skinparam linetype ortho
skinparam ranksep 110
skinparam nodesep 90
skinparam Padding 10
skinparam PackagePadding 12
skinparam NoteTextAlignment left
```

## 5. Como ajustar spacing y padding

### `ranksep`

- Rango util: `90-120`
- Sube este valor cuando las filas se pisan o cuando una nota superior queda muy pegada a la clase.
- No lo subas primero si el problema real es horizontal.

### `nodesep`

- Rango util: `70-100`
- Sube este valor cuando clases hermanas o notas laterales se montan entre si.
- Si el paquete se hace enorme, revisa primero el largo de labels y notas.

### `Padding`

- Rango util: `8-12`
- Controla el aire interno de clases y notas.
- Si el contenido se ve apretado, aumenta poco a poco.

### `PackagePadding`

- Rango util: `10-14`
- Aumenta cuando el contenido roza demasiado el borde del paquete.
- Reduce cuando el paquete mete demasiado espacio vacio y aleja notas o clases.

## 6. Reglas de redaccion de notas

- Una idea principal por nota.
- Preferible 1-3 lineas.
- Mejor frases cortas que parrafos largos.
- Si una nota supera 3 lineas, primero prueba resumirla.
- En diagramas arquitectonicos, explica el por que o la responsabilidad, no los detalles de implementacion minimos.

## 7. Validacion minima

Antes de dar por bueno un diagrama:

1. Renderiza a SVG.
2. Verifica que las notas siguen visibles en el SVG.
3. Comprueba que la asociacion nota-clase es inmediata a simple vista.
4. Revisa si algun paquete quedo artificialmente enorme.
5. Si tuviste que probar muchas combinaciones, guarda la regla aprendida en la skill.
