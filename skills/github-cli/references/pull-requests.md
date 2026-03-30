# Pull Requests (`gh pr`)

La gestión de Pull Requests mediante GitHub CLI es una de sus características más potentes. Permite a los desarrolladores evitar interrupciones de contexto cambiando entre la terminal y el navegador.

## Comandos Principales

- `gh pr list`: Muestra una lista de los pull requests abiertos en el repositorio actual. Puedes usar flags como `--state merged` o `--author "@me"`.
- `gh pr create`: Crea un pull request. Usa `--fill` para autollenar el título y descripción basados en el commit y la rama.
- `gh pr checkout <number>`: Descarga y cambia a la rama de un PR específico localmente. Ideal para revisar código.
- `gh pr diff`: Muestra las diferencias (diff) del PR actual directamente en la terminal.
- `gh pr merge`: Mezcla (merge) el PR activo. Permite seleccionar interactiva o explícitamente el tipo de merge (`--squash`, `--rebase`, `--merge`).
- `gh pr review`: Permite aprobar, solicitar cambios o comentar un PR mediante la terminal. `--approve` para aprobar directamente.
- `gh pr status`: Muestra el estado de los PRs creados por ti, los que tienes asignados para revisión y su estado de CI/CD.

## Casos de Uso Comunes

**Revisión Completa de un PR:**
1. `gh pr list` (Buscar el número del PR)
2. `gh pr checkout 123`
3. (Correr test localmente y revisar código)
4. `gh pr review --approve -b "Se ve bien, buen trabajo."`
5. `gh pr merge --squash --delete-branch`
