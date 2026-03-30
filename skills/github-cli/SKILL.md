---
name: github-cli
description: Experto en el uso de GitHub CLI (gh). Utiliza esta skill para conocer los comandos principales de gh, gestionar pull requests, issues, repositorios y autenticación desde la terminal, aplicando las mejores prácticas de automatización y flujos de trabajo en GitHub.
---

# GitHub CLI (gh) Expert Skill

Esta skill proporciona una guía experta para el uso de la herramienta de línea de comandos `gh`, permitiendo a los desarrolladores y agentes interactuar fluidamente con GitHub sin salir de la terminal.

## Capacidades y Flujos de Trabajo
El uso de `gh` agiliza en gran medida las operaciones habituales. Consulta las referencias detalladas para cada área de operación:

### 1. Gestión de Pull Requests (PRs)
- **Referencia:** [Pull Requests (`gh pr`)](references/pull-requests.md)
- **Uso común:** Creación de PRs, revisión, mergeo y validación de integraciones (CI).
- *Ejemplo rápido:* `gh pr create --fill` para crear un PR usando los commits recientes y el nombre de la rama.

### 2. Gestión de Issues
- **Referencia:** [Issues (`gh issue`)](references/issues.md)
- **Uso común:** Visualización, comentario y cierre de incidencias directamente.
- *Ejemplo rápido:* `gh issue view 123 --web` abre el issue en el navegador.

### 3. Gestión de Repositorios
- **Referencia:** [Repositorios (`gh repo`)](references/repositories.md)
- **Uso común:** Creación, clonación, forkeo y revisión de repositorios.
- *Ejemplo rápido:* `gh repo clone cli/cli` para clonar un repositorio rápidamente.

### 4. Automatización y Autenticación
- **Referencia:** [Autenticación y Alias (`gh auth` & `gh alias`)](references/automation.md)
- **Uso común:** Configuración inicial, login e inclusión en scripts (creación de alias personalizados).

## Mejores Prácticas con `gh`
- Siempre que sea posible, prefiere usar flags automatizados (como `--fill` o `--yes`) para evitar interacciones manuales en scripts de CI/CD.
- Para ver rápidamente las estadísticas de un repositorio o su README, usa `gh repo view`.
- Consulta siempre la documentación nativa usando `gh <command> --help`.
