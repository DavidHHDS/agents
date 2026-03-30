---
name: erd-guidelines
description: Directrices y reglas para la creación de Diagramas Entidad-Relación (ERD) enfocadas en bases de datos PostgreSQL con llaves primarias estandarizadas y relaciones flexibles.
---

# Guía para el Diseño de Diagramas Entidad-Relación (ERD)

Esta skill define las reglas obligatorias al momento de diseñar diagramas de entidad-relación (ERD) o esquemas de bases de datos.

## 📌 Reglas de Diseño de Base de Datos

### 1. Llaves Primarias (PK)
- **TODAS las tablas**, sin excepción alguna (incluso las tablas intermedias o de pivote), deben tener su propia clave primaria (`PK`).
- El nombre de la columna debe ser siempre `id`.
- El tipo de dato para esta columna debe ser `bigserial` (autoincremental en PostgreSQL).

### 2. Multiplicidad y Relaciones (0 a N / 0 a 1)
- Todas las relaciones (Foráneas) deben establecerse con multiplicidad que permita valores nulos del lado hijo:
  - De **0 a N** (cero a muchos)
  - De **0 a 1** (cero a uno)
- **Justificación**: La obligatoriedad funcional de una relación (ej. 1 a N, o 1 a 1 obligatorios) es una **regla de negocio**, y NO debe estar forzada el motor de base de datos o por constraints. Hacer esto promueve un diseño más resiliente y facilita considerablemente el mantenimiento, las migraciones de datos, la inserción segmentada de registros y adaptaciones de negocio futuras.

### 3. Distribución y Claridad Visual
- Los diagramas generados usando PlantUML deben **distribuir correctamente las tablas**.
- Agrupa tablas relacionadas lógicamente o por dominios.
- Usa instrucciones de espaciado o direccionalidad.
