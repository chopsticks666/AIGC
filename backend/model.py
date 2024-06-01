# backend/model.py

class Adder:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2


import os
import tempfile
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import torch


class MusicGenerator:
    def __init__(self):

        self.model_dict = {1: 'facebook/musicgen-small',
                      2: 'facebook/musicgen-medium',
                      3: 'facebook/musicgen-large',
                      4: 'facebook/musicgen-melody',
                      5: 'facebook/musicgen-melody-large'}

        self.model = MusicGen.get_pretrained(self.model_dict[1])
        self.set_duration()


    def generate_music(self, prompt, audio_file = None):
        if audio_file is not None:
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
                audio_file.save(temp_audio.name)
                melody, sr = torchaudio.load(temp_audio.name)

            os.unlink(temp_audio.name)

            wav = self.model.generate_with_chroma([prompt], melody[None], sr)
        else:
            wav = self.model.generate([prompt])

        output_filename = 'generated_music'
        audio_write(output_filename, wav[0].cpu(), self.model.sample_rate, strategy="loudness", loudness_compressor=True)

        return output_filename+'.wav'
    
    def change_to_model(self, model_id=1):
        try:
            if self.model is not None:
                del self.model  # 删除当前模型对象
                torch.cuda.empty_cache()  # 清理CUDA缓存
            self.model = MusicGen.get_pretrained(self.model_dict[model_id])
            if self.model is None:
                print("Failed to load model:", self.model_dict[model_id])
            else:
                self.set_duration()  # Ensure we set parameters only if the model is successfully loaded
        except Exception as e:
            print("Error loading model:", str(e))

    
    def set_duration(self, duration = 8):
        self.model.set_generation_params(duration=duration)
        