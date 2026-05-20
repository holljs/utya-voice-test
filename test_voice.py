import os
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
# Автоматически скачает легкие веса модели (~99 МБ)
tts = TTS(auto_download=True)

# Выбираем женский голос F1 (наша Утя)
style = tts.get_voice_style(voice_name="F3")

# Текст с тегом эмоции <laugh> для смешка/радости
text = "Привет, мой хороший! <laugh> Утя очень рада тебя видеть! Давай скорее играть?"

print(f"Синтез текста: {text}")
wav, duration = tts.synthesize(
    text=text,
    lang="ru",
    voice_style=style,
    total_steps=10,
    speed=1.18
)

output_file = "utya_test.wav"
tts.save_audio(wav, output_file)
print(f"Успех! Аудиофайл сохранен как {output_file} (Длительность: {duration[0]:.2f} сек.)")
