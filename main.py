from utils import predict_process
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile
import os
import shutil
from datetime import datetime as dt
import logging
import torch
import traceback
import uvicorn

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

current_file_path = os.path.abspath(__file__)
current_dir  = os.path.dirname(current_file_path)


app = FastAPI()

origins = [
    "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



@app.post("/upload")
async def main(file: UploadFile = UploadFile(...)):
    """
    generate Yolo object detection
     **Args file**:\n
    `file` (file) : input image or video.
    return {'path': 'output path'}
    """
    

    try:
        parrent_directory = os.path.join(current_dir, "input")
        base = dt.now().strftime('%H%M%S')
        store_path = os.path.join(parrent_directory, base)
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        if  os.path.exists(store_path):
            shutil.rmtree(store_path)
        logger.info('Create input directory')
        os.mkdir(store_path)
        file_path = f"{store_path}/{file.filename}"
        with open(file_path, "wb") as dest_file:
            shutil.copyfileobj(file.file, dest_file)
        result = predict_process(file_path)
        torch.cuda.empty_cache()
        shutil.rmtree(store_path)

        return {"path":result}
    except Exception as e:
            error_message = traceback.format_exc()
            logger.info(error_message)
            return e
    
if __name__=="__main__":
    uvicorn.run(app, port=7373, host='0.0.0.0')