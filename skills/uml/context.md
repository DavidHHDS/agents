- # Guía Completa de Diagramación UML con PlantUML
	- El Lenguaje Unificado de Modelado (UML) es el estándar de la industria para el modelado y diseño de software. Esta guía detalla los diagramas más utilizados, su teoría, los tipos de relaciones y ejemplos prácticos utilizando la notación de PlantUML.
	- ## 1. Diagrama de Casos de Uso
		- ### Teoría:
			- Los diagramas de casos de uso describen el comportamiento del sistema desde el punto de vista del usuario (o "actor"). No se centran en cómo se hace algo a nivel técnico, sino en qué hace el sistema. Son fundamentales para la recolección de requisitos y para definir los límites del sistema.
		- ### Tipos de Relaciones y Cuándo Usarlas:
			- **Asociación (Comunicación):** Conecta a un actor con un caso de uso en el que participa.
				- **Cuándo usarla:** Cuando un usuario interactúa directamente con una función del sistema (ej. Cliente -> Iniciar Sesión).
			- **Inclusión (<<include>>):** Un caso de uso base incorpora explícitamente el comportamiento de otro caso de uso.
				- **Cuándo usarla:** Para evitar duplicar código/pasos. Si "Pagar" siempre requiere "Validar Tarjeta", entonces "Pagar" incluye a "Validar Tarjeta".
			- **Extensión (<<extend>>):** Un caso de uso añade comportamiento a un caso de uso base, pero solo bajo ciertas condiciones.
				- **Cuándo usarla:** Para comportamientos opcionales o manejo de errores. Ej. "Pagar" puede ser extendido por "Aplicar Cupón de Descuento".
			- **Generalización (Herencia):** Un actor o caso de uso hereda de otro más general.
				- **Cuándo usarla:** Cuando tienes un actor "Usuario" y uno más específico "Administrador" que puede hacer todo lo del usuario y más.
		- ### Ejemplo PlantUML:
			-
			  ```plantuml
			  @startuml
			  skinparam actorStyle hollow
			  skinparam noteBackgroundColor lightyellow
			  left to right direction
			  
			  actor "Cliente" as cliente
			  actor "Administrador" as admin
			  
			  rectangle "Sistema de E-Commerce" {
			    usecase "Realizar Compra" as UC_Compra
			    usecase "Validar Pago" as UC_Validar
			    usecase "Aplicar Descuento" as UC_Descuento
			    usecase "Gestionar Inventario" as UC_Inventario
			  }
			  
			  cliente --> UC_Compra
			  admin --> UC_Inventario
			  
			  ' Relación de inclusión
			  UC_Compra ..> UC_Validar : <<include>>
			  note right of UC_Validar
			    <b><<include>> Obligatorio</b>
			    Siempre que se compra,
			    el sistema DEBE validar el pago.
			  end note
			  
			  ' Relación de extensión
			  UC_Descuento .u.> UC_Compra : <<extend>>
			  note bottom of UC_Descuento
			    <b><<extend>> Opcional</b>
			    Solo se aplica si el 
			    cliente introduce un cupón.
			  end note
			  
			  ' Generalización de actores
			  admin -|> cliente : <<generalization>>
			  note top of admin
			    El Administrador "es un" Cliente.
			    Puede hacer todo lo del Cliente
			    más sus propias acciones.
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774295965057_0.svg)
	- ## 2. Diagrama de Clases
		- ### Teoría:
			- Es el diagrama principal para el modelado estructural. Muestra la estructura estática del sistema detallando las clases, sus atributos, métodos y las relaciones entre los objetos. Es el plano directo para la Programación Orientada a Objetos (POO).
		- ### Explicación Detallada de las Relaciones:
			- Las relaciones en un diagrama de clases definen cómo se comunican y dependen los objetos entre sí. Se miden generalmente por su nivel de acoplamiento (qué tan dependiente es una clase de otra) y el ciclo de vida de los objetos.
			- **Dependencia (..> flecha punteada abierta):**
				- **Nivel de acoplamiento:** Muy débil.
				- **Concepto:** Una clase "usa" a otra transitoriamente. Si la clase B cambia, la clase A podría verse afectada, pero A no contiene a B como atributo.
				- **Implementación en código:** Se da cuando un objeto de la clase B se pasa como parámetro a un método de la clase A, se crea localmente dentro de un método de A, o es el tipo de retorno de un método.
				- **Ejemplo:** Una clase Impresora depende de un Documento solo en el momento en que se llama al método imprimir(Documento doc).
			- **Asociación (--> flecha sólida abierta):**
				- **Nivel de acoplamiento:** Moderado.
				- **Concepto:** Es una relación estructural donde una clase "conoce" a la otra. Tienen ciclos de vida independientes, pero se comunican constantemente.
				- **Implementación en código:** La clase A tiene un atributo del tipo de la clase B.
				- **Ejemplo:** Un Profesor y un Estudiante. El profesor conoce a sus estudiantes, pero si el profesor es despedido, el estudiante sigue existiendo.
			- **Agregación (o-- rombo vacío):**
				- **Nivel de acoplamiento:** Moderado-Fuerte.
				- **Concepto:** Es un tipo especial de asociación que representa una relación "Todo-Parte". Sin embargo, las partes pueden existir de forma independiente del todo.
				- **Implementación en código:** La clase contenedora recibe las instancias de las partes a través de su constructor o setters (Inyección de dependencias), lo que significa que fueron creadas fuera de ella.
				- **Ejemplo:** Un Equipo y sus Jugadores. Si el equipo se disuelve, los jugadores siguen existiendo y pueden unirse a otro equipo.
			- **Composición (*-- rombo lleno):**
				- **Nivel de acoplamiento:** Muy Fuerte.
				- **Concepto:** Es una relación "Todo-Parte" estricta. Las partes NO pueden existir independientemente del todo. El contenedor es el único responsable de la creación y destrucción de sus partes.
				- **Implementación en código:** Las instancias de las partes se instancian dentro del constructor del contenedor. Si el contenedor es recolectado por el Garbage Collector, las partes también lo serán.
				- **Ejemplo:** Una Casa y una Habitación. Si la casa es demolida, las habitaciones que la componen dejan de existir inevitablemente.
			- **Herencia / Generalización (<|-- flecha triangular vacía):**
				- **Nivel de acoplamiento:** Extremo (El acoplamiento más fuerte posible).
				- **Concepto:** Representa una relación "Es un" (Is-A). Una clase hija hereda la estructura (atributos) y el comportamiento (métodos públicos/protegidos) de una clase padre abstracta o concreta.
				- **Ejemplo:** Un Perro es un Animal.
			- **Realización / Implementación (<|.. flecha triangular punteada):**
				- **Concepto:** Una clase se compromete a implementar un contrato definido por una Interfaz. La interfaz dicta qué se debe hacer (firma de métodos), y la clase define cómo hacerlo.
				- **Ejemplo:** Un Teclado implementa la interfaz IDispositivoEntrada.
		- ### Ejemplo PlantUML:
			-
			  ```plantuml
			  @startuml
			  skinparam noteBackgroundColor lightyellow
			  
			  abstract class Vehiculo {
			    # marca: String
			    + arrancar()
			  }
			  
			  interface IConducible {
			    + frenar()
			  }
			  
			  class Auto {
			    - modelo: String
			    + conducir()
			    + recargar(gas: Gasolina)
			  }
			  
			  class Motor {
			    - cilindrada: int
			  }
			  
			  class Conductor {
			    - nombre: String
			  }
			  
			  class Gasolina {
			    - octanaje: int
			  }
			  
			  ' 1. Herencia / Generalización
			  Vehiculo <|-- Auto
			  note on link
			    <b>Herencia (Generalización):</b>
			    Relación "Es un". El Auto hereda los
			    atributos (#marca) y métodos (+arrancar) 
			    de la clase padre Vehiculo. Permite la
			    reutilización y el polimorfismo.
			  end note
			  
			  ' 2. Realización / Implementación
			  IConducible <|.. Auto
			  note on link
			    <b>Realización (Interfaces):</b>
			    El Auto "firma un contrato" con 
			    IConducible. Está obligado a programar 
			    la lógica exacta del método frenar().
			  end note
			  
			  ' 3. Composición
			  Auto *-- "1" Motor : contiene >
			  note on link
			    <b>Composición (Todo-Parte fuerte):</b>
			    Ciclo de vida atado. El Motor es 
			    instanciado DENTRO del Auto. Si el 
			    objeto Auto es eliminado de la memoria, 
			    su Motor también se destruye.
			  end note
			  
			  ' 4. Agregación
			  Conductor o-- "1" Auto : maneja >
			  note on link
			    <b>Agregación (Todo-Parte débil):</b>
			    Ciclo de vida independiente. El Conductor 
			    tiene una referencia al Auto, pero el Auto 
			    fue creado por fuera. Si el Auto choca 
			    y se destruye, el Conductor sobrevive.
			  end note
			  
			  ' 5. Dependencia
			  Auto ..> Gasolina : usa >
			  note on link
			    <b>Dependencia (Uso temporal):</b>
			    Acoplamiento más débil. El Auto no 
			    guarda a la Gasolina como un atributo. 
			    Solo la recibe temporalmente como 
			    parámetro en el método recargar(gas).
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774296040144_0.svg)
	- ## 3. Diagrama de Componentes
		- ### Teoría:
			- Muestra la organización y las dependencias entre los componentes de software (módulos, librerías, bases de datos, APIs). Ayuda a visualizar cómo se ensamblan las piezas del sistema a un nivel macro o arquitectónico.
		- ### Tipos de Relaciones y Cuándo Usarlas:
			- **Interfaz Proporcionada (Lollipop ()--):** El componente ofrece un servicio hacia afuera.
				- **Cuándo usarla:** Cuando tu componente tiene una API pública que otros pueden consumir.
			- **Interfaz Requerida (Socket )--):** El componente necesita un servicio de otro componente para funcionar.
				- **Cuándo usarla:** Cuando tu componente depende de una Base de Datos o una API externa.
			- **Dependencia (..>):** Un componente depende de otro.
				- **Cuándo usarla:** Para conectar una interfaz requerida con una proporcionada de otro componente.
		- ### Ejemplo PlantUML:
			-
			  ```plantuml@startuml
			  @startuml
			  skinparam componentStyle uml2
			  skinparam noteBackgroundColor lightyellow
			  skinparam nodesep 100
			  skinparam ranksep 100
			  
			  package "Frontend Web" {
			    [Aplicación React] as WebApp
			  }
			  
			  package "Backend Microservicios" {
			    [Microservicio Pagos] as Pagos
			    [Microservicio Usuarios] as Usuarios
			  }
			  
			  database "Cluster PostgreSQL" as BD
			  
			  ' Declaración de Interfaces proporcionadas (Usando palabra clave interface para evitar solapamiento)
			  interface "API_Users"
			  interface "API_Pagos"
			  
			  ' Conectando componentes a sus interfaces (Proporcionan)
			  API_Users - Usuarios
			  API_Pagos - Pagos
			  
			  ' El Frontend REQUIERE estas interfaces (Dependencia)
			  WebApp ..> API_Users : usa
			  WebApp ..> API_Pagos : usa
			  
			  ' Los microservicios dependen de la base de datos
			  Usuarios ..> BD : JDBC / SQL
			  Pagos ..> BD : JDBC / SQL
			  
			  note left of WebApp
			    El Frontend desconoce la lógica 
			    interna de los microservicios;
			    solo depende de sus <b>interfaces (APIs)</b>.
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774297055549_0.svg)
	- ## 4. Diagrama de Actividades
		- ### Teoría:
			- Modela el flujo de control o flujo de datos (work flow) de un proceso o un caso de uso. Es similar a un diagrama de flujo avanzado, pero soporta la ejecución paralela y concurrente. Es ideal usar "Calles" (Swimlanes) para identificar quién hace qué.
		- ### Tipos de Relaciones y Cuándo Usarlas:
			- **Transición (-->):** El paso de una actividad a otra.
				- **Cuándo usarla:** Para definir el orden secuencial lógico de las acciones.
			- **Bifurcación / Decisión (Rombo if/else):** Evalúa una condición y divide el flujo en caminos mutuamente excluyentes.
				- **Cuándo usarla:** Cuando el flujo cambia según una regla de negocio.
			- **Sincronización (Fork / Join - fork/end fork):** Divide el flujo en múltiples caminos que se ejecutan al mismo tiempo (en paralelo) y luego los vuelve a unir.
				- **Cuándo usarla:** Cuando varias tareas independientes pueden ejecutarse simultáneamente (ej. Mientras se empaqueta, también se genera la factura).
		- ### Ejemplo PlantUML:
			-
			  ```plantuml
			  @startuml
			  skinparam noteBackgroundColor lightyellow
			  
			  |#LightCyan|Cliente|
			  start
			  :Añadir productos al carrito;
			  :Proceder al pago;
			  
			  |#LightYellow|Sistema Web|
			  if (¿Hay stock suficiente?) then (Sí)
			    :Calcular total;
			    
			    |#LightGreen|Pasarela de Pagos|
			    :Procesar tarjeta de crédito;
			    
			    |#LightYellow|Sistema Web|
			    fork
			      :Generar Factura Digital;
			    fork again
			      |#LightPink|Almacén|
			      :Empacar productos;
			      :Entregar a paquetería;
			    end fork
			    
			    |#LightYellow|Sistema Web|
			    :Enviar email de confirmación;
			  
			  else (No)
			    |#LightYellow|Sistema Web|
			    :Mostrar error "Sin Stock";
			  endif
			  
			  |#LightCyan|Cliente|
			  :Recibir notificación final;
			  stop
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774297367178_0.svg)
	- ## 5. Diagrama de Secuencia
		- ### Teoría:
			- Muestra cómo los objetos interactúan entre sí a lo largo del tiempo para llevar a cabo una tarea. Se enfoca en el orden cronológico (de arriba hacia abajo) en el que se envían los mensajes.
		- ### Tipos de Relaciones y Cuándo Usarlas:
			- **Mensaje Síncrono (-> flecha sólida):** El emisor espera a que el receptor termine de procesar el mensaje para continuar.
				- **Cuándo usarlo:** Llamadas a métodos, consultas HTTP bloqueantes, o consultas a base de datos.
			- **Mensaje de Retorno (--> flecha punteada):** La respuesta a un mensaje síncrono.
				- **Cuándo usarlo:** Para devolver el valor de la ejecución.
			- **Mensaje Asíncrono (->> flecha abierta):** El emisor envía el mensaje y continúa su trabajo sin esperar.
				- **Cuándo usarlo:** Llamadas a colas de mensajería (RabbitMQ), procesos en segundo plano.
			- **Fragmentos Combinados (alt, opt, loop):** Permiten modelar lógica compleja.
				- **Cuándo usarlos:** alt para IF/ELSE, opt para un condicional simple, loop para iteraciones (for/while).
		- ### Ejemplo PlantUML:
			-
			  ```plantuml
			  @startuml
			  autonumber
			  skinparam maxMessageSize 100
			  skinparam noteBackgroundColor lightyellow
			  
			  box "Capa Cliente" #LightCyan
			  actor Usuario
			  participant "Navegador Web" as UI
			  end box
			  
			  box "Capa Servidor" #LightYellow
			  participant "API Gateway" as API
			  participant "AuthService" as Auth
			  database "Base de Datos" as BD
			  end box
			  
			  Usuario -> UI : Ingresar credenciales
			  activate UI
			  
			  UI -> API : POST /login (Síncrono)
			  activate API
			  
			  API -> Auth : validarToken(user, pass)
			  activate Auth
			  
			  Auth -> BD : SELECT user FROM users
			  activate BD
			  BD --> Auth : result_set (Retorno)
			  deactivate BD
			  
			  alt Credenciales Correctas
			      Auth --> API : JWT Token Generado
			      API --> UI : 200 OK + Token
			      UI -> Usuario : Redirigir al Dashboard
			  else Credenciales Incorrectas
			      Auth --> API : Error 401
			      API --> UI : 401 Unauthorized
			      UI -> Usuario : Mostrar mensaje de error
			  end
			  
			  deactivate Auth
			  deactivate API
			  deactivate UI
			  
			  note right of Auth
			    <b>Fragmento "alt":</b>
			    Evalúa condiciones excluyentes.
			    Equivale a un bloque "if / else"
			    en programación.
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774297483358_0.svg)
	- ## 6. Diagrama Entidad-Relación (ER)
		- ### Teoría:
			- Aunque históricamente pertenece al modelado de bases de datos relacionales y no a UML estricto, PlantUML lo soporta mediante la notación "Crow's Foot" (Pata de Gallo). Describe las entidades (tablas), sus atributos (columnas) y las relaciones estructurales entre ellas.
		- ### Tipos de Relaciones (Multiplicidad/Cardinalidad) y Cuándo Usarlas:
			- **Uno a Uno (||--||):** Una entidad A se relaciona solo con una entidad B.
				- **Cuándo usarla:** Para separar datos muy grandes o sensibles de una tabla principal (ej. Usuario y sus Datos Biométricos).
			- **Uno a Muchos (||--o{ o ||--|{):** Una entidad A se relaciona con muchas B.
				- **Cuándo usarla:** Es la más común. Ej. Un Cliente tiene muchas Facturas, pero la Factura es de un solo Cliente. (El círculo o indica "Cero o muchos", la línea | indica "Uno o muchos").
			- **Muchos a Muchos (}o--o{):** Entidades de ambos lados pueden tener múltiples relaciones mutuas.
				- **Cuándo usarla:** Fases de diseño conceptual. En diseño físico, esta relación siempre requiere romperse creando una "tabla intermedia".
		- ### Ejemplo PlantUML:
			-
			  ```plantuml@startuml
			  hide circle
			  skinparam linetype ortho
			  skinparam noteBackgroundColor lightyellow
			  skinparam nodesep 120
			  skinparam ranksep 120
			  skinparam entityBackgroundColor white
			  skinparam entityBorderColor black
			  
			  entity "Cliente" as cliente {
			    * id_cliente : INT <<PK>>
			    --
			    * nombre : VARCHAR(50)
			    * email : VARCHAR(100)
			  }
			  
			  entity "Pedido" as pedido {
			    * id_pedido : INT <<PK>>
			    --
			    * id_cliente : INT <<FK>>
			    * fecha : DATETIME
			    estado : VARCHAR(20)
			  }
			  
			  entity "Producto" as producto {
			    * id_producto : INT <<PK>>
			    --
			    * descripcion : VARCHAR(255)
			    * precio : DECIMAL
			  }
			  
			  entity "Pedido_Detalle" as detalle {
			    * id_pedido : INT <<FK>>
			    * id_producto : INT <<FK>>
			    --
			    * cantidad : INT
			  }
			  
			  ' Relaciones
			  cliente ||--o{ pedido
			  pedido ||--|{ detalle
			  producto ||--o{ detalle
			  
			  ' Notas posicionadas fuera de las entidades
			  note top of cliente
			    <b>1 a Muchos (0..N):</b>
			    Un cliente realiza 0
			    o múltiples pedidos.
			  end note
			  
			  note right of pedido
			    <b>1 a Muchos (1..N):</b>
			    Un pedido contiene al
			    menos 1 detalle obligatorio.
			  end note
			  
			  note bottom of producto
			    <b>1 a Muchos (0..N):</b>
			    Un producto puede estar
			    en 0 o muchos pedidos.
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774298017414_0.svg)
	- ## 7. Agrupación y Organización (Paquetes)
		- ### Teoría:
			- A medida que los diagramas crecen (especialmente en sistemas corporativos y arquitecturas robustas), se vuelve indispensable organizar sus elementos. En UML, un Paquete (Package) es un contenedor lógico que permite agrupar elementos semánticamente relacionados (como clases, entidades, casos de uso, componentes o incluso otros paquetes).
			- El uso de paquetes ayuda a:
				- Modularizar el sistema.
				- Definir "espacios de nombres" (namespaces).
				- Controlar la visibilidad.
				- Visualizar la arquitectura a un alto nivel (como en las arquitecturas limpias o el Diseño Guiado por el Dominio - DDD).
			- PlantUML permite usar paquetes en casi cualquier tipo de diagrama. Además de la palabra clave package, soporta visualizaciones lógicas equivalentes y gráficamente distintas como folder, frame, node, cloud, database o rectangle.
		- ### Cuándo Usar Paquetes:
			- **Organización Arquitectónica:** Para separar responsabilidades lógicas. Ejemplo: aislar la Interfaz de Usuario, la Lógica de Negocio (Casos de Uso/Dominio) y la Capa de Acceso a Datos (Infraestructura).
			- **Agrupación Funcional:** Para dividir un sistema masivo en módulos manejables (ej. "Módulo de Recursos Humanos", "Módulo de Contabilidad", "Módulo de Inventario").
			- **Manejo de Dependencias Macroscópicas:** Para ilustrar con una flecha de dependencia (..>) que todo un módulo depende de otro (ej. Todos los "Casos de Uso" dependen del "Dominio").
		- ### Ejemplo PlantUML (Arquitectura por Capas agrupando diferentes elementos):
			-
			  ```plantuml@startuml
			  skinparam noteBackgroundColor lightyellow
			  skinparam packageStyle rectangle
			  
			  ' --- DEFINICIÓN DE PAQUETES ---
			  
			  package "UI / Capa de Presentación" as UI {
			    class VistaLogin
			    class ControladorUsuarios {
			      + registrarUsuario()
			    }
			  }
			  
			  package "Capa de Aplicación" as App {
			    ' Agrupando un Caso de Uso dentro de un paquete
			    usecase "Crear Cuenta (Caso de Uso)" as UC_CrearCuenta
			  }
			  
			  package "Capa de Dominio" as Domain {
			    ' Agrupando Entidades y Modelos de Negocio
			    entity "Usuario" as EntidadUsuario {
			      + id: UUID
			      + email: String
			    }
			    class ReglasValidacion {
			      + esMayorDeEdad()
			    }
			  }
			  
			  package "Capa de Infraestructura" as Infra {
			    ' Anidando estructuras (Folder dentro de Package)
			    folder "Bases de Datos" {
			      class UsuarioRepositoryImpl {
			        + guardar(Usuario u)
			      }
			    }
			  }
			  
			  ' --- RELACIONES Y DEPENDENCIAS ENTRE PAQUETES ---
			  
			  ' La UI invoca a la capa de Aplicación
			  ControladorUsuarios ..> UC_CrearCuenta : invoca >
			  
			  ' La capa de Aplicación usa el Dominio
			  UC_CrearCuenta ..> EntidadUsuario : crea >
			  UC_CrearCuenta ..> ReglasValidacion : valida >
			  
			  ' La capa de Infraestructura implementa e interactúa con el Dominio
			  UsuarioRepositoryImpl ..> EntidadUsuario : persiste >
			  
			  ' Marcando una dependencia general a nivel de paquete
			  App ..> Infra : inyecta dependencias >
			  
			  note right of Domain
			    <b>Núcleo del Sistema:</b>
			    Al agrupar el Dominio en su propio
			    paquete, visualizamos claramente que
			    está aislado. No tiene flechas salientes
			    hacia Infraestructura o UI.
			  end note
			  @enduml
			  ```
			- ![diagram.svg](../assets/diagram_1774298391435_0.svg)
