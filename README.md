# Client Registerer

## Tarea 4

Crear un Login de usuarios donde se podrán ingresar con usuario y contraseña (al
escribir la contraseña esta debe ocultarse), si el usuario no está registrado se podrá
registrar ingresando los siguientes campos (nombre de usuario, nombre, apellido,
número de teléfono, correo electrónico, contraseña, confirmar contraseña). Cuando
el usuario accede ingresando una contraseña y un usuario ya registrado se cierra la
ventana de login y se muestra una ventana diferente con un listado de todos los
usuarios registrados, sus nombres, número de teléfono y correo electrónico.

## Configurar servidor local de desarrollo

### Requisitos

- Python >= 3.10

### Pasos:

1. Tener python instalado (3.10 al menos).
2. Instalar las dependencias que estan en `requirements.txt`
3. Correr las migraciones con `python manage.py migrate`
4. Correr el servidor local con `python manage.py runserver`
