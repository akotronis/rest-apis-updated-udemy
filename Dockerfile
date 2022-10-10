FROM python:3.10
EXPOSE 5000
WORKDIR /app
# COPY app.py db.py requirements.txt ./
COPY . .
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]