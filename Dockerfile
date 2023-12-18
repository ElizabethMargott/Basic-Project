# Utiliza una imagen base adecuada para tu proyecto Django
FROM python:3.11

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de tu proyecto
RUN pip install -r requirements.txt

# Ejecuta las migraciones de Django
RUN python manage.py migrate

# Inicia el servidor Gunicorn
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
