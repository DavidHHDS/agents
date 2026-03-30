# Formato de SKILL.md (Frontmatter)

El archivo `SKILL.md` DEBE contener un bloque YAML frontmatter al inicio.

### Campos Requeridos
- `name`: Identificador único (coincide con la carpeta).
- `description`: Qué hace la skill y cuándo usarla.

### Campos Opcionales
- `license`: Licencia del código.
- `compatibility`: Requisitos del sistema (ej. `Requires Python 3.10+`).
- `metadata`: Mapa de llave-valor para datos adicionales.
- `allowed-tools`: (Experimental) Herramientas pre-aprobadas.

### Ejemplo de Bloque Frontmatter
```yaml
---
name: my-cool-skill
description: Does X when Y happens. Use this for Z tasks.
license: MIT
metadata:
  version: "1.0.0"
  author: "Expert"
---
```
