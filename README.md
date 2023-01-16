# CRUD-with-Flask-SQLAlchemy-PostgreSQL

Sistema de contactos con Flask SQLAlchemy y PostgreSQL

### Descargar el repositorio y configuraciones
En la consola se escribe:
```sh
git clone https://github.com/ec4m/CRUD-with-Flask-SQLAlchemy-PostgreSQL.git
```
Posteriormente se entra en la carpeta del proyecto, se crea el entorno virtual y se activa:
```sh
python3 -m venv env
source env/bin/activate
```
Se instalan las dependencias del proyecto con:
```sh
pip3 install -r requirements.txt
```
### Creación de la base de datos
Dentro de ContactModel se encuentra la declaración de la tabla contact_model, asi que no hay necesidad de generarla desde postgresql.

### Configuración de variables de entorno
Se debe crear un archivo .env para escribir las variables de entorno necesarias para la configuración del servidor y la conexión a la base de datos, se puede crear con el comando:
```sh
touch .env
```
O por medio de Vscode y se establecen las siguientes variables segun la cuenta de postgres a la que se vincule y el nombre de la database:
```
PGSQL_USER = tu_usuario_postgres
PGSQL_PASSWORD = tu_password_postgres
PGSQL_HOST = tu_host_servidor 
PGSQL_DATABASE = tu_database
```

### Lanzamiento del servidor
Desde la consola se lanza el servidor por medio del comando:
```sh
python3 src/app.py
```

### Para acceder a la app se usa la url:
```
http://localhost:3000/contact/
```
#### En caso de utilizar un servidor experno se usa con su respectivo dominio:
```
http://<dominio>/contact/
```
