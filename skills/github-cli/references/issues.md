# Issues (`gh issue`)

La herramienta `gh issue` facilita el seguimiento de errores, de características y la discusión desde tu entorno de desarrollo local.

## Comandos Principales

- `gh issue list`: Lista los issues. Soporta varios flags para filtrar como `--assignee "@me"`, `--label "bug"`, `--state all`.
- `gh issue create`: Inicia un flujo interactivo (o automatizado mediante flags `--title`, `--body`) para reportar un nuevo issue.
- `gh issue view <number>`: Lee los detalles de un issue o imprime sus comentarios (`--comments`). Sirve mucho para recordar el contexto sin abrir Github.
- `gh issue comment <number>`: Agrega un comentario a un issue existente (`--body "texto"`).
- `gh issue close <number>`: Cierra el issue indicado. Permite especificar la razón: `--reason "completed"` o `--reason "not planned"`.
- `gh issue edit <number>`: Edita etiquetas, asignados o hitos (milestones) de un issue.

## Casos de Uso Comunes

**Abordar y Cerrar un Bug:**
1. `gh issue list --label bug` (Listar bugs pendientes)
2. `gh issue view 42` (Revisar los detalles del reporte)
3. (Trabajar en el código, crear commit)
4. `gh issue close 42 -m "Se corrigió en el último commit"`
