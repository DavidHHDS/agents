# Autenticación y Automatización (`gh auth` & `gh alias`)

La gestión inteligente de `gh` implica aprovechar bien la autenticación y atajos de teclado.

## Autenticación

- `gh auth login`: Inicia el flujo de autenticación, es necesario antes de hacer cualquier cosa. Puede autenticarse mediante web (muy cómodo) o usar un Personal Access Token.
- `gh auth status`: Comprueba si estás conectado en los hosts activos. Útil antes de ejecutar scripts para confirmar el estado de sesión.

## Alias y Atajos

`gh` te permite definir alias (comandos personalizados combinando sub-comandos u otras llamadas).
- `gh alias set <name> <command>`
  - Ejemplo: `gh alias set co "pr checkout"` (El comando por defecto `gh co <number>` lo provee internamente la herramienta).
- `gh alias list`: Para ver qué alias están definidos y qué hacen.

## Integraciones y Variables de entorno

Se pueden invocar comandos en modo crudo usando la API de github para cualquier cosa que el CLI todavía no soporte:
- `gh api repos/{owner}/{repo}`: Ejecuta un request en formato REST de forma fácil haciendo uso de la autenticación de `gh`.

Además para CI, se puede pasar el environment `GH_TOKEN` para ejecutar `gh` sin un entorno de usuario humano interactivo.
