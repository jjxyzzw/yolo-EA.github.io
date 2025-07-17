from sahi.predict import predict

predict(
    model_type="ultralytics",
    model_path=r"D:\Desktop\yolo\Run\yolo11s-C2PSAiEMA-AFPN4Head_final\weights\best.pt",
    model_device="cuda:0",  # or 'cuda:0'
    model_confidence_threshold=0.5,
    source=r"D:\Desktop\yolo\YOLOv11\Dataset\Photo",
    slice_height=640,
    slice_width=640,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2,
    visual_bbox_thickness=1
)