# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run --name flask-api-cont -p 5000:5000 -w /app -v ${PWD}:/app flask-smorest-api sh -c "flask run"
```
