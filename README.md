# Red-Social / REDSON
Aplicación web de una Red social con Django

### Para utilizarlo/configurarlo:

1. Crear una carpeta 
```
mkdir redsocial
```
2. Ingrese a la carpeta creada
```
cd redsocial
```
3. Clona el repositorio o descargalo como zip.
```
git clone https://github.com/ramic0/Red-Social.git
```
4. Ingrese a la carpeta Red-Social
```
cd Red-Social
```
5. Crea un ambiente virtual
```
python -m venv redsonenv
```
6. Activa el ambiente virtual / windows
```
redsonenv\scripts\activate
```
7. Instala las dependencias/librerias en requirements.txt
```
pip install -r requirements.txt
```
8. Ejecuta las migraciones.
```
python manage.py makemigrations 
```
```
python manage.py migrate
```

9. Crea un superusuario.
```
python manage.py createsuperuser
```

10. Corre el servidor.
```
python manage.py runserver
```
### Nota
***
Seguridad.
> El código presentado no colocar en producción por lo que la clave secret esta expuesta es decir esta pública y todo el usuario que descarge el código tiene la misma clave. 
> Si desea utilizar el código para producción cambiar la clave secret.
