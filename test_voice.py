import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === СТИШКИ ДЛЯ КОМНАТЫ "ДА И НЕТ" ===
    
   # ✅ Ответ ДА
    "yesno_walk.wav": """Мы наде́енем босоно́ошки,
Побежии́м мы по доро́шке.
Све́тит со́лнце нам всегдаа́.
Де́тки зво́нко кри́кнут!!"""
}

print(f"Запуск озвучки {len(quiz_phrases)} фраз...")

for filename, text in quiz_phrases.items():
    print(f"Синтез: {filename}")
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
