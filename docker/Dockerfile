FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY tests tests

CMD ["pytest", "--cov=app", "--cov-report=term", "--cov-report=xml:coverage.xml"]
