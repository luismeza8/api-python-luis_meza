# api-python-luis_meza

## Notas importantes:

- Utilice Django Rest Framework, PostgreSQL y JWT para esta api.

- La api esta alojada en un vps de digital ocean, de esta manera esta lista para su uso en produccion.

- La url base es: https://api-python.luis_meza.dev/api/v1/

- Agregue el certificado SSL para mayor seguridad y al final de la url el v1 para simular una api mas robusta.

- Un detalle importante, hice todo el codigo en ingles excepto por los modelos, ya que en el archivo que me enviaron estos estaban español y los endpoints en ingles asi que para seguir el formato del archivo lo hice de esta manera, espero y no haya ningun problema

- En el documento se menciona el uso de DTOs, en el caso de DRF estos podrian equivaler a los serializers de cada modelo, lo aclaro por las dudas

- En caso de que por alguna razon este fallando la api que esta en produccion, por favor haganmelo saber para arreglarlo lo antes posible.

## Como correr el proyecto de forma local

1.- Clonar localmente el repositorio desde github:

```
git clone https://github.com/luismeza8/api-python-luis_meza
```

2.- Entrar a la carpeta

```
cd api-python-luis_meza
```

3.- Meter el archivo .env adjunto en el correo a esta carpeta (se que estar enviando archivos .env no es seguro pero al ser esta una demostracion considero que se vale)

4.- Ejecutar el comando:

```
docker compose up --build
```

El archivo docker-compose.yml ya incluye el comando para hacer las migraciones entonces si todo ha salido bien el proyecto se deberia de estar ejecutando en 0.0.0.0:8000

## Como correr las prubeas unitarias

1.- Una vez que se haya construido los contenedores se tiene que correr el siguiente comando para que se inicien en segundo plano

```
docker compose up -d
```

2.- Ya que el contenedor este corriendo hay que ejecutar el siguiente comando:

```
docker compose exec web python manage.py test
```

Esto prueba todos los endpoints de Usuarios y Productos de forma automatica

## Comandos para probar la api

### Crear un nuevo usuario de acceso

- Los endpoints especificados en el documento para Products y Users estan protegidos por lo que se necesita primero generar un token creando un nuevo usuario con el cual acceder a la api (este usuario es ajeno al model Usuarios que pide en el documento)

```
curl -X POST https://api-python.luismeza.dev/api/v1/auth/registration/ \
-H "Content-Type: application/json" \
-d '{
    "username": "usuarioprueba",
    "email": "usuario@prueba.com",
    "password1": "un-password-seguro",
    "password2": "un-password-seguro"
}'
```

### Login

- Una vez creado el usuario es necesario loggearse en la api

```
curl -X POST https://api-python.luismeza.dev/api/v1/auth/login/ \
-H "Content-Type: application/json" \
-d '{
    "username": "usuarioprueba",
    "password": "un-password-seguro"
}'
```

- Esta llamada retorna tu token con el cual se puede acceder a los endpoints protegidos

## Products

### Crear un producto

- Se debe de cambiar '<TU_TOKEN>' por el token que retorne en login

```
curl -X POST https://api-python.luismeza.dev/api/v1/products/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Mouse",
    "precio": "250",
    "stock": 150
}'
```

### Listar productos

```
curl -X GET https://api-python.luismeza.dev/api/v1/products/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

### Obtener un producto en especifico

```
curl -X GET https://api-python.luismeza.dev/api/v1/products/<ID_DEL_PRODUCTO>/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

### Actualizar un producto

```
curl -X PUT https://api-python.luismeza.dev/api/v1/products/<ID_DEL_PRODUCTO>/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Mouse Pro",
    "precio": "300",
    "stock": 125
}'
```

### Actualizar parcialmente un producto

```
curl -X PATCH https://api-python.luismeza.dev/api/v1/products/<ID_DEL_PRODUCTO>/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "activo": false
}'
```

### Eliminar un producto

```
curl -v -X DELETE https://api-python.luismeza.dev/api/v1/products/<ID_DEL_PRODUCTO>/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

## Usuarios

### Crear un usuario

```
curl -X POST https://api-python.luismeza.dev/api/v1/users/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "fulanito",
    "apellido": "de tal",
    "edad": 28
}'
```

### Obtener todos los Usuarios

```
curl -X GET https://api-python.luismeza.dev/api/v1/users/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

### Obtener un usuario en especifico

```
curl -X GET https://api-python.luismeza.dev/api/v1/users/<ID_DEL_USUARIO>/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

### Actualizar un usuario

```
curl -X PUT https://api-python.luismeza.dev/api/v1/users/<ID_DEL_USUARIO>/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "juan",
    "apellido": "perez",
    "edad": 29
}'
```

### Actualizar parcialmente un usuario

```
curl -X PATCH https://api-python.luismeza.dev/api/v1/users/<ID_DEL_USUARIO>/ \
-H "Authorization: Bearer <TU_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "activo": false
}'
```

### Eliminar un usuario

```
curl -v -X DELETE https://api-python.luismeza.dev/api/v1/users/<ID_DEL_USUARIO>/ \
-H "Authorization: Bearer <TU_TOKEN>"
```

Esta es mi API, espero que sea de su agrado, gracias.

