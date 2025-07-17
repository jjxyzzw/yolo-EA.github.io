---

# 高空航拍视角下的脐橙树目标识别检测（YOLO-EA）

## 📌 项目简介

本项目基于YOLOv11提出了一种改进的轻量化目标检测模型 —— **YOLO-EA**，专注于解决高空航拍图像中脐橙树检测任务中存在的小目标识别难、复杂背景干扰强和实时性要求高等问题。项目引入了**C2PSA-iEMA注意力机制**、**AFPN特征融合网络**及**EIoU损失函数**等创新组件，并结合**SAHI切片辅助推理**策略，显著提升了小目标检测精度和鲁棒性。

## 🌟 模型特点

* 🧠 **C2PSA-iEMA Attention**：融合倒置残差结构与动态注意力机制，增强特征表达能力；
* 🧱 **AFPN (Asymptotic Feature Pyramid Network)**：渐近式多尺度特征融合，提升模型对不同尺度目标的适应能力；
* 🎯 **EIoU Loss**：替代传统CIoU，优化边界框回归效果，提高收敛速度；
* ✂️ **SAHI切片推理**：支持超远距离航拍图像下的小目标检测，有效降低漏检率。

## 📊 实验结果

| 模型      | FPS    | 中等距离航拍脐橙树识别数目 |
| -------- |  --------- | ---  |
| YOLOv11s |  115.6     | 90   |
| YOLO-EA  | 43         | 151  |

> 注：数据采集自赣南师范大学果园，分辨率4000×3000，结合公开数据集进行训练与验证。

## 📁 项目结构

```
├── datasets/           # 数据集及标注（使用Roboflow平台增强）
├── models/             # YOLO-EA模型定义（含iEMA, C2PSA, AFPN模块）
├── train.py            # 模型训练脚本
├── predict.py          # 检测推理脚本（含sahi切片）
├── utils/              # 工具函数：损失函数、可视化、评估等
├── configs/            # 超参数与模型配置文件
├── README.md           # 项目说明文档
└── results/            # 示例结果（检测图、热力图、评估指标）
```

## 🚀 快速开始

### 环境依赖

* Python 3.10+
* PyTorch 2.4.1 + CUDA 12.1
* `ultralytics`, `sahi`, `opencv-python`, `matplotlib`, `timm`, `einops`

```bash
# 安装依赖
conda create -n yolo-ea python=3.10
conda activate yolo-ea
pip install -r requirements.txt
```

### 训练模型

```bash
python train.py --data data.yaml --imgsz 640 --epochs 600 --batch 48 --device 0
```

### 推理与检测（含SAHI）

```bash
python predict.py --weights yolov11-ea.pt --source path/to/image.jpg --sahi
```

## 🔍 可视化样例

| 原图                     | YOLOv11s                  | YOLO-EA               |
| ---------------------- | ------------------------- | --------------------- |
| ![原图](results/raw.jpg) | ![v11s](results/v11s.jpg) | ![EA](results/ea.jpg) |

## 📚 引用本项目

如果你在研究中使用了本项目，请引用本论文：

```
zzw, 等. 高空航拍视角下的脐橙树目标识别检测[J]. 国防科技大学学报, 2025.
```

## 🧠 致谢

感谢导师在设备支持、无人机航拍图像采集与论文指导方面提供的帮助！感谢Roboflow平台提供公开训练数据支持。

---

