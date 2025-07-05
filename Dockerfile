FROM python:3.10-slim

# Install dependencies for building TgCrypto
RUN apt-get update && apt-get install -y gcc python3-dev build-essential

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy rest of the files
COPY . .

CMD python3 main.py
