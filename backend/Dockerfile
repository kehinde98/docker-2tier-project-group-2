FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

COPY app.py .

CMD ["gunicorn", "--bind", "0.0.0.0:8081", "app:app"]