import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# ---------- ВОПРОСЫ ДЛЯ ИГРЫ: УТЯ ДЕЙСТВУЕТ ----------
quiz_phrases = {
    "qact_run.wav": "Где Уутя бежи́т?",
    "qact_swing.wav": "Покажи́, где Уутя кача́ется?",
    "qact_wash.wav": "Где Уутя мо́ется?",
    "qact_play.wav": "Покажи́, где Уутя игра́ет?",
    "qact_cry.wav": "Где Уутя пла́чет?",
    "qact_jump.wav": "Покажи́, где Уутя пры́гает?",
    "qact_talk.wav": "Где Уутя разгова́ривает?",
    "qact_laugh.wav": "Покажи́, где Уутя смеё́тся?",
    "qact_dance.wav": "Где Уутя танцуует?"
}

print(f"Запуск озвучки {len(quiz_phrases)} вопросов...")

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

print("✅ Успех! Все вопросы для игры с Утей готовы!")
