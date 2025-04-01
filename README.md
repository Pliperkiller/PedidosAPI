
# PedidosAPI

## Descripción
PedidosAPI es un microservicio diseñado para gestionar el ciclo de vida de los pedidos en una cadena de restaurantes. Este proyecto sigue una arquitectura basada en capas (Domain, Application, Infrastructure) y utiliza principios de **Domain-Driven Design (DDD)** para modelar entidades, objetos de valor y servicios.

## Autors
**pliperkiller**
**diazd525**
**gjoiver**
## Requisitos
- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **PostgreSQL** (base de datos)

## Estructura del Proyecto
```plaintext
src/
├── domain/                 # Capa de dominio
│   ├── entities/           # Entidades del dominio
│   ├── value_objects/      # Objetos de valor
│   ├── ports/              # Interfaces de repositorios y servicios
│   └── exceptions/         # Excepciones específicas del dominio
├── application/            # Capa de aplicación
│   ├── usecases/           # Casos de uso
│   ├── dtos/               # Data Transfer Objects (DTOs)
│   └── services/           # Servicios de aplicación
├── infrastructure/         # Capa de infraestructura
│   ├── adapters/           # Adaptadores de entrada/salida
│   │   ├── web/            # Adaptadores web
│   │   │   ├── blueprints/ # Blueprints de Flask
│   │   └── persistence/    # Adaptadores de persistencia
│   │       ├── models/     # Modelos de la base de datos
│   │       └── repositories/ # Repositorios de persistencia
│   ├── config/             # Configuración de la aplicación
└── tests/                  # Pruebas unitarias e integración
```

## Instalación

### 1. Clonar el repositorio
```sh
git clone https://github.com/Pliperkiller/PedidosAPI.git
cd PedidosAPI
```

### 2. Crear un entorno virtual
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate para cmd o venv\Scripts\Activate.ps1 en powershell
```

### 3. Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Copia el archivo `.env.example` y renómbralo como `.env`:
```sh
cp .env.example .env
```

Edita el archivo `.env` y actualiza las variables necesarias:
```plaintext
DATABASE_URI=postgresql://user:password@localhost:5432/nombre_base_datos
FLASK_ENV=development
```

### 5. Configurar la base de datos
1. Asegúrate de que PostgreSQL esté instalado y en ejecución.
2. Crea una base de datos para el proyecto:
   ```sql
    CREATE USER boss WITH PASSWORD 'bosspass';
    CREATE DATABASE pedidos_db;
    GRANT ALL PRIVILEGES ON DATABASE pedidos_db TO boss;
    ALTER DATABASE pedidos_db OWNER TO boss;
   ```

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


### **Endpoints configurados**

#### **1. Crear un pedido**
- **URL**: `/pedidos`
- **Método**: `POST`
- **Descripción**: Permite crear un nuevo pedido con los datos del cliente, dirección de entrega y los items solicitados.
- **Cuerpo de la solicitud**:
  ```json
  {
    "id_cliente": "123",
    "direccion_entrega": {
      "calle": "Calle Principal",
      "ciudad": "Ciudad",
      "codigo_postal": "12345"
    },
    "items": [
      {"producto_id": "456", "cantidad": 2},
      {"producto_id": "789", "cantidad": 1}
    ]
  }
  ```
- **Respuesta exitosa**:
  ```json
  {
    "id_pedido": "abc123",
    "estado": "CREADO",
    "total": 150.00
  }
  ```

---

#### **2. Verificar el estado general de la API**
- **URL**: `/health`
- **Método**: `GET`
- **Descripción**: Verifica si la API está funcionando correctamente.
- **Respuesta exitosa**:
  ```json
  {
    "status": "ok",
    "message": "API is running"
  }
  ```

---

#### **3. Verificar el estado de la base de datos**
- **URL**: `/db-health`
- **Método**: `GET`
- **Descripción**: Verifica si la conexión con la base de datos está activa.
- **Respuesta exitosa**:
  ```json
  {
    "status": "ok",
    "database": "connected"
  }
  ```


## Tecnologías Utilizadas
- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para la gestión de la base de datos.
- **Pydantic**: Validación de datos.
- **Alembic**: Migraciones de base de datos.
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
