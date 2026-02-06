FROM debian:latest

RUN apt-get update -y 


RUN apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    ca-certificates \
    libssl-dev \
    libsasl2-dev \
    build-essential \
    cmake \
    swig \
    pkg-config

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
COPY certs/ ./certs/

RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


COPY app .


RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5671

CMD ["sh", "-c", "python3 -u main.py & tail -f /dev/null"]