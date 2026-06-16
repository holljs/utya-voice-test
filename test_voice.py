import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === ВВОДНАЯ ФРАЗА (ДЛЯ ПЕРВОЙ КАРТИНКИ С ОКНОМ) ===
    "st_intro.wav": "Привет! Давай вместе сочиниим смешнуую сказку! Слушай внимательно и сам выбирай, что будет дальше!",

    # === ИСПРАВЛЕННЫЙ ШАГ 1 (Где зонтик и кастрюля) ===
    "st_q1.wav": "Ой, на улице сильный дождь! Что мы возьмём с собой, чтобы не промокнуть?"
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
        # Магия Ути-Те (частота 54000)
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
