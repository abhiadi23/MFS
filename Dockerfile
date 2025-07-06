FROM python:3.10-slim

# System dependencies for Pyrogram and TgCrypto
RUN apt-get update && apt-get install -y gcc build-essential ffmpeg

# Set workdir
WORKDIR /app

# Copy requirement file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Render uses port passed via $PORT env, though Telegram bots don’t need a port
EXPOSE 10000

# Start the bot
CMD ["python3", "main.py"]