import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# ---------- ВСЕ ФРАЗЫ ДЛЯ СОРОБАНА ----------
# Ударения расставлены: ´ после гласной. Ударная "У" удвоена без знака ударения.
quiz_phrases = {
    # --- Тайный Орден Пяти (Задания) ---
    "anime_brothers_3_2.wav": "Три и два — бра́тья!",
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
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все файлы для 'Нейро-Гения' готовы к скачиванию!")
