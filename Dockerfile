FROM tiangolo/uvicorn-gunicorn:python3.11-slim

LABEL maintainer="Jared Ratner <OrangeB0lt>"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

EXPOSE 8000
EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--reload","--host", "0.0.0.0", "--port", "5000"]