FROM python:3.8

# Copiar los archivos de la aplicación a /app
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Configurar las variables de entorno
ENV DJANGO_SETTINGS_MODULE=project.settings

# Ejecutar la aplicación
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
