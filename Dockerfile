FROM python:3.10
WORKDIR /app
# COPY app.py db.py requirements.txt ./
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["qunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]