# Repositories (`gh repo`)

Los comandos de tipo `gh repo` son la base para el manejo del proyecto general y la inicialización rápida de directorios.

## Comandos Principales

- `gh repo clone <owner>/<repo>`: Clona un proyecto usando su nombre (y la autenticación asociada al CLI) en lugar de buscar la URL entera.
- `gh repo create`: Si estás en un contenedor Git local nuevo, este comando interactivo te permite publicarlo a GitHub (como un nuevo repositorio remoto en tu cuenta o una organización).
- `gh repo fork`: Crea un fork del repositorio actual (o uno especificado) en tu propia cuenta de GitHub y opcionalmente lo clona inmediatamente (`--clone`).
- `gh repo view`: Imprime un resumen del repositorio que estás viendo, y el README actual si lo tiene.
- `gh repo sync`: Sincroniza el repositorio local (y forkeado) con el origen o el repositorio "upstream" principal.

## Casos de Uso Comunes

**Iniciar un nuevo proyecto:**
1. `mkdir mi-proyecto && cd mi-proyecto`
2. `git init`
3. `gh repo create mi-proyecto --public --source=. --remote=origin` (Crea repositorio remoto y lo añade como origen)
4. `git add . && git commit -m "Initial commit"`
5. `git push -u origin HEAD`
