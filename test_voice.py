import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS для Сказки 2...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

story_phrases = {
    # === ИНТРО И ФИНАЛ СКАЗКИ ===
    "st_q1.wav": "На у́лице пошёл до́ждик! Что Уу́тя возьмёт с собо́й?",
    "st2_a5_abs.wav": "А́й-а́й-а́й, как ко́лется! На ка́ктусе спа́ть соверше́нно невозмо́жно!"
}

print(f"Запуск синтеза {len(story_phrases)} файлов для Сказки 2...")

for filename, text in story_phrases.items():
    print(f"Генерация: {filename}")
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
        print(f"❌ Ошибка в {filename}: {e}")

print("✅ Все файлы озвучки для Сказки 2 готовы!")
