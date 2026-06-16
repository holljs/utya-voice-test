import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === ШАГ 4 ===
    "st_q4.wav": "Мы переплыли лужу и встретили голодную собачку. Чем мы её угостиим?",
    "st_a4_norm.wav": "Вкуусная косточка! Собавчка очень рада и виляет хвоостиком!",
    "st_a4_abs.wav": "Ой..ой! Собачки не едяят старые башмакииии! Она его пожеваала и выплюнула!",
    # === ФИНАЛ ===
    "st_end.wav": "Молодец! Какая смешнааая скаазка у нас получилась!"
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
