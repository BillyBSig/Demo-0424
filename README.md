# Demo

## About
This repository contains an implementation of the Yolo object detection model's inference. The endpoint requires uploading an image or video. The code will automatically detect our device (CPU/CUDA). If our device is using CPU, the code will utilize the ONNX model (.onnx), and if our device is using GPU, it will employ the PyTorch model (.pt).


## Installation

- clone the repository `git clone https://github.com/BillyBSig/Demo-0424.git`

- download the YOLO model following these link
    - pytorch model https://drive.google.com/file/d/1FKzxILrtQlQ-wLK_AmxvhjtKl-Yhmakc/view?usp=sharing
    - onnx model https://drive.google.com/file/d/1LpBmCS7WUSdrRZFHkiFfgmmsujzQInNO/view?usp=sharing
- Put these model in `model` directory

    ├── Lmodel/
    |   ├── yolov8n.onnx
    |   ├── yolov8n.pt


- run the code on CLI `uvicorn main:app --host 0.0.0.0 --port 7373 --reload`

- The end point will serve locally in http://127.0.0.1:7373/upload

## Docker instruction
- build the docker image
    `docker build -t yolo_api .`
- run the docker following this step:
    - Create and/or copy the output directory that contain the video or image output process
        e.g:

            D:\YoloDemo\detect

    - if we use the **GPU cuda**, run
            `docker run --gpus all -d  -p 7373:7373 -v local//output-detect:app/detect/ --name yolo_api_serve yolo_api`
        - change the `local//output-detect` with our local output directory
            e.g : 
            `docker run --gpus all -d  -p 7373:7373 -v D:\YoloDemo\detect:app/detect/ --name yolo_api_serve yolo_api`
        - the output will using the internal docker path
            e.g:

                {
                "path": "/app/detect/2024-04-21-153032/meeting.jpg"
                }
        Then in our local device, output will save in `local output directory/2024-04-21-153032/meeting.jpg`
    - if we use the **CPU only**, then run
            `docker run -d  -p 7373:7373 -v loca//output-detect:app/detect/ --name yolo_api_serve yolo_api`
        - change the `local//output-detect` with our local output directory
            e.g : 
                `docker run -d  -p 7373:7373 -v D:\YoloDemo\detect:app/detect/ --name yolo_api_serve yolo_api`  

