FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
