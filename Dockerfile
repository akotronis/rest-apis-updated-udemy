FROM python:3.10
WORKDIR /app
# COPY app.py db.py requirements.txt ./
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["/bin/bash", "docker-entrypoint.sh"]