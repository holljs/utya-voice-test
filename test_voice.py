import os
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

# Берем самый высокий из доступных женских голосов (F4)
style = tts.get_voice_style(voice_name="F4")

text = "Привет, мой хороший! <laugh> Утя очень рада тебя видеть! Давай скорее играть?"

print("Синтез базового голоса...")
wav, duration = tts.synthesize(
    text=text,
    lang="ru",
    voice_style=style,
    total_steps=10,
    speed=1.1 # Чуть ускоряем базовый темп
)

# Сохраняем промежуточный вариант
temp_file = "temp_adult.wav"
tts.save_audio(wav, temp_file)

print("Применяем магию: делаем голос детским (Pitch Shift)...")
final_file = "utya_test.wav"

# Команда ffmpeg для поднятия тона (коэффициент 1.35 делает голос мультяшным)
# asetrate поднимает тон, atempo возвращает нормальную скорость произношения
os.system(f'ffmpeg -y -i {temp_file} -af "asetrate=44100*1.35,aresample=44100,atempo=1/1.35" {final_file}')

print(f"Готово! Мультяшная Утя сохранена как {final_file}")
