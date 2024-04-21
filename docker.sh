docker build -t yolo_api . 
docker run -d  -p 7373:7373 -v loca//output-detect:app/detect/ --name yolo_api_serve yolo_api
docker run --gpus all -d  -p 7373:7373 -v loca//output-detect:app/detect/ --name yolo_api_serve yolo_api