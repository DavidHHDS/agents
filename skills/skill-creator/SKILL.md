---
name: skill-creator
description: Experto en creación y estructuración de Skills para Claude Code siguiendo la especificación oficial de agentskills.io. Usa esta skill para generar nuevas capacidades de agente, refactorizar skills existentes o validar estructuras de directorios.
---

# Skill Creator (Experto en Especificaciones)

Esta skill te guía en la creación de nuevas capacidades para agentes siguiendo la especificación oficial de [agentskills.io](https://agentskills.io/specification).

## Guía de Configuración
Antes de crear una skill, revisa las especificaciones detalladas:
- [Estructura de Directorios](references/directory-spec.md): Carpetas `references/`, `assets/` y `scripts/`.
- [Formato de SKILL.md](references/frontmatter-spec.md): Validación de frontmatter (`name`, `description`).
- [Revelación Progresiva](references/directory-spec.md#revelación-progresiva): Cómo optimizar el uso de tokens.

## Flujo de Trabajo
1. **Identificar la necesidad**: Define el `name` (slug) y la `description` clara.
2. **Inicializar estructura**: Crea la carpeta y los subdirectorios recomendados.
3. **Generar Manifiesto**: Escribe el `SKILL.md` con el frontmatter correcto.
4. **Distribuir Contenido**: Mueve la teoría a `references/` y los ejemplos/código a `assets/`.

## Activos Disponibles
- [Plantilla de Inicio](assets/starter-template.md): Un esqueleto listo para copiar y pegar.

---
*Referencia oficial: [https://agentskills.io/specification](https://agentskills.io/specification)*
