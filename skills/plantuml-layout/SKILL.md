---
name: plantuml-layout
description: Reglas y utilidades para distribuir diagramas PlantUML con notas cercanas, espaciado legible y render estable a SVG. Usar al crear o ajustar diagramas de clases, componentes, secuencia u otros diagramas PlantUML.
---

# PlantUML Layout

Usa esta skill cuando necesites:

- crear un diagrama PlantUML nuevo con una base de layout consistente;
- corregir notas que quedan demasiado lejos de sus clases;
- ajustar distribucion, espaciado o padding sin romper la legibilidad;
- renderizar a SVG e inspeccionar rapidamente el resultado.

## Flujo recomendado

1. Empieza con la base de `assets/skinparam-starter.puml`.
2. Organiza primero clases, paquetes y relaciones; agrega notas al final.
3. Para cada nota, evalua arriba, izquierda, abajo y derecha; deja la nota en el espacio libre mas cercano que no cruce relaciones ni tape otras clases.
4. Si una nota empuja demasiado el layout, acorta el texto antes de seguir agregando padding.
5. Renderiza con `scripts/render-svg.sh`.
6. Inspecciona el SVG con `scripts/inspect-svg-layout.py` y luego valida visualmente.

## Reglas rapidas

- Prefiere rutas cortas en nombres de paquetes si los labels con puntos abren demasiado el diagrama.
- Usa notas cortas: idealmente 1-3 lineas y una idea principal por nota.
- Reserva notas laterales para clases de borde y notas superiores para abstracciones centrales con espacio vertical disponible.
- Si una clase queda en una zona muy densa, es mejor omitir la nota en ese diagrama que forzar una conexion larga y confusa.
- Ajusta `ranksep`, `nodesep` y `PackagePadding` de uno en uno; no muevas todo al mismo tiempo.

## Recursos

- Reglas detalladas: `references/layout-rules.md`
- Base reutilizable de skinparams: `assets/skinparam-starter.puml`
- Render generico a SVG: `scripts/render-svg.sh`
- Inspeccion generica de entidades/notas en SVG: `scripts/inspect-svg-layout.py`
