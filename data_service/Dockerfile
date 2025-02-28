FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt . 
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["python3", "app.py"]


