# Red-Social / REDSON
Aplicación web de una Red social con Django

### Para utilizarlo/configurarlo:

1. Clona el repositorio o descargalo como zip.
```
git clone https://github.com/ramic0/Red-Social.git
```

2. Crea un ambiente virtual
```
python -m venv redsonenv
```
3. Activa el ambiente virtual / windows
```
redsonenv\scripts\activate
```
4. Instala las dependencias/librerias en requirements.txt
```
pip install -r requirements.txt
```
5. Ejecuta las migraciones.
```
python manage.py makemigrations 
python manage.py migrate
```

6. Crea un superusuario.
```
python manage.py createsuperuser
```

7. Corre el servidor.
```
python manage.py runserver
```
### Nota
***
Seguridad.
> El código presentado no colocar en producción por lo que la clave secret esta expuesta es decir esta pública y todo el usuario que descarge el código tiene la misma clave. 
> Si desea utilizar el código para producción cambiar la clave secret.
