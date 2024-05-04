# AIGC for Songs
多媒体课程project
## 环境搭建

Notes: pytorch 2.1.0 cuda 12.1

```python
## 创建aigc环境
conda create -n aigc python=3.10 pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia

# 进入环境
conda activate aigc

# 下载音频库
pip3 install -U audiocraft  # stable release

# 下载flask
pip3 install flask

# 运行
python frontend.py
```


## Continuing

1. 用户根据自己的需求选择模型


2. 模型本地存储



