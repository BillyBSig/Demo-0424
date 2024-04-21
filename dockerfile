FROM python:3.10-slim
# RUN apt-get update && apt-get install -y ffmpeg build-essential

RUN mkdir -p /root/.config/Ultralytics/
ADD https://ultralytics.com/assets/Arial.ttf /root/.config/Ultralytics/
ADD https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

# RUN apt-get update \
#     && apt install -y libgl1-mesa-glx \
#     && apt install libglib2.0-0

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    zip \
    curl \
    htop \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libpython3-dev \
    gnupg \
    g++ \
    libusb-1.0-0 \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*


#     && apt-get install -y libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev \
#     && apt-get -y install libpq-dev gcc \
#     && pip install psycopg2

WORKDIR /app
RUN pip install --upgrade pip

RUN pip uninstall torch torchaudio -y
RUN pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121
COPY requirements.txt .
RUN pip install  -r requirements.txt
COPY . .

EXPOSE 7373
RUN mkdir /detect


CMD ["sh", "-c","uvicorn main:app --host 0.0.0.0 --port 7373 --reload"]