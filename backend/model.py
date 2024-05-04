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

class MusicGenerator:
    def __init__(self):
        self.model = MusicGen.get_pretrained('facebook/musicgen-melody')
        self.model.set_generation_params(duration=8)  # generate 8 seconds.

    def generate_music(self, audio_file, prompt):
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
            audio_file.save(temp_audio.name)
            melody, sr = torchaudio.load(temp_audio.name)

        os.unlink(temp_audio.name)

        wav = self.model.generate_with_chroma([prompt], melody[None], sr)

        output_filename = 'generated_music'
        audio_write(output_filename, wav[0].cpu(), self.model.sample_rate, strategy="loudness", loudness_compressor=True)

        return output_filename+'.wav'