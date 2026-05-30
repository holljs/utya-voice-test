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
    "brother4_task.wav": "Прибавля́ем четы́ре: тут нужна́ Короле́ва Пять, и ухо́дит брат четырё́х — оди́н.",
    "brother3_task.wav": "Прибавля́ем три: тут нужна́ Короле́ва Пять, и ухо́дит брат тро́йки — два.",

    # --- Тайный Орден Пяти (Комиксы) ---
    "anime_intro_five.wav": "О́рден Пяти́!",
    "anime_brothers_4_1.wav": "Четы́ре и оди́н — бра́тцы!",
    "anime_brother4_step1.wav": "Как приба́вить четы́ре? Буусинок внизуу не хвата́ет!",
    "anime_brother4_step2.wav": "Туут нужна́ Короле́ва Пять! Опуска́ем буусинку вниз!",
    "anime_brother4_step3.wav": "Ми́нус оди́н! Малы́ш ухо́дит отдыха́ть!"
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
