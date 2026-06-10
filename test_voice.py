import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # --- Лайфхаки: Магия на 5 (Твой алгоритм с ноликом) ---
    "magic5_2.wav": "Молодец!",
    "magic5_3.wav": "МОЛОДЕЦ!!",
    "magic5_4.wav": "Молодееец!",
    "magic5_5.wav": "Молодеец!!!",
    "magic5_6.wav": "Мо-ло-деец!",
    "molodec.wav": "Молодеец!!!!"
}

print(f"Запуск озвучки {len(quiz_phrases)} фраз...")

for filename, text in quiz_phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7 
        )
        # Вернули правильную частоту 24000!
        sf.write(filename, wav.squeeze(), 24000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
