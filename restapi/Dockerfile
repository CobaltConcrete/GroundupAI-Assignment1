FROM python:3.11-slim

WORKDIR /app

# Copy dependencies first (better caching)
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 10000

CMD ["uvicorn", "my_rest_api:app", "--host", "0.0.0.0", "--port", "10000"]