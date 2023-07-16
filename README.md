# Proyecto Blog BookStore Academy

El proyecto es un blog, tiene muchas funcionalidades, blog, edicion(post, agregar cursos, agregar libros), gestion de usuarios( creacion de usuario mediante el registro) y la autenticacion de usuarios.

Link al video demostracion 3min: https://drive.google.com/file/d/1C1_8yGL9J1HOisPSATydQOOBdh-R3wky/view?usp=sharing

## Características

- Registro de usuarios
- Inicio de sesión y cierre de sesión
- Creación y edición de blogs.
- Comentarios en los blogs
- Creacion, edicion y eliminacion cursos y libros.
- Página "Acerca de mí" personalizada
- Interfaz de administración para gestionar la aplicación y los datos

## Adiciones

- trabajo con API propia para cargue de los cursos en Espanol.

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/millertsu1/ProyectoFinalPython_Ladino.git

2. Accede al directorio del proyecto:

cd /sistema

3. Realiza las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate


6. Inicia el servidor de desarrollo:

python manage.py runserver

7. Accede a la aplicación en tu navegador web en la siguiente dirección:

http://localhost:8000/ y.o 127.0.0.1:8080

NOTA
Es posble que tengas que instalar CKeditor y CrispyForms:
- la primera es para permitir editar el post con texto RICH TEXT( agregar negrita, cursiva... etc). Link https://pypi.org/project/django-ckeditor/
- la segunda es para que los formularios tengan estilos predeterminados de Boostrap5. Link https://pypi.org/project/django-crispy-forms/ 
- los comandos pip install django-ckeditor y pip install django-crispy-forms


## Tecnología Utilizada

## Front-End
HTML
Javascript
Bootstrap 
## Back-End

Python 
Django
Json 

## Casos de Prueba

Este repositorio incluye una carpeta `CasosDePruebas` donde se encuentran documentados diferentes casos de prueba para verificar el funcionamiento de las funcionalidades del proyecto.
