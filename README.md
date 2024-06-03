# AIGC for Songs
多媒体课程project

## 代码结构

├── backend
│   ├── __pycache__
│   ├── models
│   │   ├── __init__.py
│   │   ├── model.py
│   ├── utils.py
├── static
│   ├── background_sustech.jpg
│   ├── campus_scenery.jpg
│   ├── iMed_background.png
│   ├── iMed.png
│   ├── xiaohui.png
├── templates
│   ├── about_us.html
│   ├── generate_music.css
│   ├── generate_music.html
│   ├── github.html
│   ├── index.html
│   ├── result.html
│   ├── test_page.html
├── frontend.py
├── generated_music.wav
├── image copy 2.png
├── image copy.png
├── image.png
├── README.md
└── web.config

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

查看演示视频: [demo_video.mp4](demo.mp4)

