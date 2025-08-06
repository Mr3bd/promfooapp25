# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

ENV OPENAI_API_KEY=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
EXPOSE 8888

CMD ["python", "main.py"]
