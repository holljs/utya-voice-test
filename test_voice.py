import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

phrases = {
    "w_drink.wav": "Хочу пить.",
    "w_eat.wav": "Хочу кушать.",
    "w_give.wav": "Дай это!",
    "w_help.wav": "Помоги́.",
    "w_cartoon.wav": "Включи́ мультик.",
    "w_walk.wav": "Пойдём гуля́ть.",
    "w_more.wav": "Хочу ещё!",
    "w_play.wav": "Пойдём игрáть.",
    "w_read.wav": "Пойдём читáть.",
    "w_potty.wav": "На горшóк.",
    "w_yes.wav": "Да.",
    "w_no.wav": "Нет.",
    "w_sleep.wav": "Хочу спать."
}

print(f"Запуск озвучки {len(phrases)} карточек желаний...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    wav, duration = tts.synthesize(
        text=text,
        lang="ru",
        voice_style=style,
        total_steps=10,
        speed=0.7 
    )
    sf.write(filename, wav.squeeze(), 54000)

print("✅ Готово! Все хотелки озвучены чисто и без багов.")
