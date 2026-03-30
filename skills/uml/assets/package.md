# Ejemplo: Arquitectura por Paquetes

```plantuml
@startuml
skinparam packageStyle rectangle

package "Capa de Presentación (UI)" as UI {
  class ControladorUsuarios
}

package "Capa de Aplicación" as App {
  usecase "Crear Cuenta" as UC_CrearCuenta
}

package "Capa de Dominio" as Domain {
  entity "Usuario" {
    + id: UUID
  }
}

package "Capa de Infraestructura" as Infra {
  folder "Base de Datos" {
    class UsuarioRepositoryImpl
  }
}

' La presentación usa los casos de uso
ControladorUsuarios ..> UC_CrearCuenta : invoca >

' Casos de uso manipulan dominio
UC_CrearCuenta ..> Usuario : crea >

' Infraestructura obedece / persiste entidades del dominio
UsuarioRepositoryImpl ..> Usuario : persiste >

@enduml
```
