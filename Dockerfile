FROM python:3.10-slim

# Install build dependencies for TgCrypto and Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    build-essential \
    libffi-dev \
    libssl-dev \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy bot files
COPY . .


# Command to run the bot
CMD ["python3", "main.py"]