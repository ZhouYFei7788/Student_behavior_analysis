import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11s.pt")

# # Train the model on the COCO8 example dataset for 100 epochs
# results = model.train(data=r"D:\py_xiangm\Car\coco.yaml", epochs=100, imgsz=640)
if __name__ == '__main__':
    results = model.train(data="coco.yaml", epochs=100, imgsz=640, batch=8, amp=True)


