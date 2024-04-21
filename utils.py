from datetime import datetime as dt
from ultralytics import YOLO
import os
import logging
import torch


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


current_file_path = os.path.abspath(__file__)
current_dir  = os.path.dirname(current_file_path)

def predict_process(target):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_path = ''
    if device == "cuda":
        model_path = os.path.join(current_dir, 'model', "yolov8n.pt")
    else:
        model_path = os.path.join(current_dir, 'model', "yolov8n.onnx")
    print(f"++++++++++++++++++{device}")
    predict = dt.now().strftime('%Y-%m-%d-%H%M%S')
    file_name = os.path.basename(target)
    result_path = os.path.join(current_dir, 'coba', predict, file_name)
    model = YOLO(model_path)
    logger.info('Predict Process')
    results = model(target, task="detect", save=True, conf=0.5, project="detect", name=predict, device=device)
    logger.info('Predict Done')


    return result_path