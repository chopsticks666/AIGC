# AIGC for Songs
多媒体课程project
## 环境搭建

Notes: pytorch 2.1.0 cuda 12.1

```python
## 创建aigc环境 
# Linux and windows
conda create -n aigc python=3.10 pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia

# Macos
conda create -n aigc python=3.10
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0


# 进入环境
conda activate aigc

# 下载音频库
pip3 install -U audiocraft  # stable release

# 下载flask
pip3 install flask

# 运行
python frontend.py
```


## demo

https://www.youtube.com/watch?v=A6X2xryjQfE

<iframe width="560" height="315" src="https://www.youtube.com/embed/A6X2xryjQfE" title="demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


