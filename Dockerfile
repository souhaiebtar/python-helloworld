FROM python:3.9-alpine
LABEL maintainer="tarhounisouhaieb@gmail.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]