import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

garden_phrases = {
    "g_win.wav": "Ура́! Ве́сь урожа́й со́бран! Ты про́сто молоде́ц!"
}

print(f"Запуск озвучки {len(garden_phrases)} фраз...")

for filename, text in garden_phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7 
        )
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все файлы для 'Нейро-Малыша' готовы к скачиванию!")
