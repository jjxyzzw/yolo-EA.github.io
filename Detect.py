import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(model=r'D:\Desktop\yolo\Run\QAQ_11s_5\weights\best.pt') # select your model.pt path
    model.predict(source=r'D:\Desktop\yolo\YOLOv11\Dataset\Photo',
                  imgsz=640,
                  project='YOLOv11/runs/detect',
                  name='QAQ_yolo11s-AFPN3',
                  save=False,
                  show=False,
                  line_width=1,
                  conf=0.5
                  # classes=1, # 是否指定检测某个类别.
                )