# Usar una imagen base de Python
FROM python:3.12

# Establecer un directorio de trabajo
WORKDIR /app

# Copiar los requerimientos del proyecto
COPY requirements.txt .

# Instalar los requerimientos del proyecto
RUN pip install -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Exponer el puerto en el que se ejecutará Django
EXPOSE 8000

# Comando para iniciar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
