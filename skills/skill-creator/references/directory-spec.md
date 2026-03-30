# Especificación de Directorios y Revelación Progresiva

Según [agentskills.io/specification](https://agentskills.io/specification), una skill debe seguir esta estructura:

### Estructura Recomendada
- `SKILL.md`: (Obligatorio) Metadatos (frontmatter) e instrucciones principales.
- `references/`: Documentación técnica detallada y guías de referencia.
- `assets/`: Plantillas, recursos estáticos, imágenes o datos.
- `scripts/`: Scripts ejecutables o herramientas de automatización.

### Revelación Progresiva
1. **Metadatos (~100 tokens)**: Se cargan al inicio de la sesión (`name`, `description`).
2. **Instrucciones (< 5000 tokens)**: El cuerpo de `SKILL.md` se carga cuando se activa la skill.
3. **Recursos (Bajo demanda)**: Los archivos en `references/`, `assets/` o `scripts/` se cargan solo cuando el agente decide leerlos.

### Reglas del `name`
- 1-64 caracteres.
- Solo minúsculas, números y guiones (`a-z`, `0-9`, `-`).
- No empezar ni terminar con guion.
- Debe coincidir con el nombre de la carpeta madre.
