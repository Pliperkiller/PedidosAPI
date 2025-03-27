# PedidosAPI

## Descripción
PedidosAPI es un microservicio diseñado para gestionar pedidos como parte de un taller de diseño dirigido por dominios (DDD). Este proyecto sigue una arquitectura basada en capas (Domain, Application, Infrastructure) y utiliza principios de DDD para modelar entidades, objetos de valor y servicios.

## Autor
**pliperkiller**

## Requisitos
- Python 3.8+
- pip (gestor de paquetes de Python)
- PostgreSQL (base de datos)

## Estructura del Proyecto
```plaintext
PedidosAPI/
├── src/                        # Código fuente
│   ├── domain/                 # Capa de dominio
│   │   ├── entities/           # Entidades del dominio
│   │   ├── value_objects/      # Objetos de valor
│   │   ├── ports/              # Interfaces de repositorios y servicios
│   │   └── exceptions/         # Excepciones específicas del dominio
│   ├── application/            # Capa de aplicación
│   │   ├── services/           # Servicios de aplicación
│   │   ├── ports/              # Puertos de entrada y salida
│   │   └── events/             # Eventos de aplicación
│   ├── infrastructure/         # Capa de infraestructura
│   │   ├── adapters/           # Adaptadores de entrada/salida
│   │   ├── config/             # Configuración de la aplicación
│   │   └── persistence/        # Repositorios de persistencia
│   └── app.py                  # Punto de entrada de la aplicación
├── tests/                      # Pruebas unitarias e integración
├── requirements.txt            # Dependencias del proyecto
├── Dockerfile                  # Configuración para contenedor Docker
└── README.md                   # Documentación del proyecto
```

## Instalación

1. **Clonar el repositorio**:
   ```sh
   git clone <repo-url>
   cd PedidosAPI
   ```

2. **Crear un entorno virtual**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**:
   - Copia el archivo `.env.example` a 

.env

.
   - Actualiza las variables necesarias, como 

DATABASE_URI

.

5. **Configurar la base de datos**:
   - Asegúrate de que PostgreSQL esté instalado y en ejecución.
   - Crea una base de datos para el proyecto.
   - Actualiza la URI de la base de datos en el archivo 

.env

.

## Uso

### Ejecutar la aplicación localmente
1. Inicia la aplicación:
   ```sh
   flask run
   ```
2. La API estará disponible en `http://localhost:5000`.

### Ejecutar con Docker
1. Construye y ejecuta el contenedor:
   ```sh
   docker-compose up --build
   ```
2. La API estará disponible en `http://localhost:5000`.

## Pruebas

### Pruebas unitarias
Ejecuta las pruebas unitarias con:
```sh
pytest
```

### Pruebas de integración
Ejecuta las pruebas de integración con:
```sh
python -m unittest discover
```

## Tecnologías Utilizadas
- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para la gestión de la base de datos.
- **Pydantic**: Validación de datos.
- **Dependency Injector**: Gestión de dependencias.
- **PostgreSQL**: Base de datos relacional.
- **Docker**: Contenedores para despliegue.

## Contribuciones
Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza un pull request.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.