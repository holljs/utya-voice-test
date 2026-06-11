import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === КАПРИЗЫ (НЕТ) ===
    "yn_q6.wav": "Мы́ игруушки разброса́ем.. Кинем всех их на́ парке́т.. Ра́зве моожно так ребяята?? Мы́ отве́тим хо́ром!!",
    "yn_no1.wav": "не́т!",
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
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
