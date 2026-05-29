import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# ---------- КОМНАТА: УТЯ ДЕЙСТВУЕТ ----------
phrases = {
    "act_run.wav": "Уутя бежи́т! И я бегуу!",
    "act_swing.wav": "Уутя кача́ется! Ка́ч-ка́ч!",
    "act_wash.wav": "Уутя мо́ется! Бууль-бууль!",
    "act_play.wav": "Уутя игра́ет! И я игра́ю!",
    "act_cry.wav": "Уутя пла́чет... Уу-уу-уу...",
    "act_jump.wav": "Уутя пры́гает! И я пры́гаю!",
    "act_talk.wav": "Уутя разгова́ривает! Бла-бла-бла!",
    "act_laugh.wav": "Уутя смеё́тся! Ха-ха-ха!",
    "act_dance.wav": "Уутя танцуует! И я танцуую!"
} # <--- Теперь всё открыто и закрыто как надо!

print(f"Запуск озвучки {len(phrases)} фраз...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7
        )
        # Сохраняем файл на диск
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все новые звуковые файлы успешно сгенерированы в текущую папку.")
