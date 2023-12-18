# Usar una imagen base de Python
FROM python:3.11-slim-buster

# Establecer un directorio de trabajo
WORKDIR /app

# Instalar las dependencias de Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . .

# Comando para iniciar el servidor de Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi"]
