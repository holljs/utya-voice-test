import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

phrases = {
    "f_cat.wav": "Кошка куушает.",
    "f_dog.wav": "Собака кушает.",
    "f_cow.wav": "Корова кушает.",
    "f_horse.wav": "Лошадь кушает.",
    "f_sheep.wav": "Овца кушает.",
    "f_pig.wav": "Свинья кушает.",
    "f_goat.wav": "Коза кушает.",
    "f_wolf.wav": "Волк кушает.",
    "f_goose.wav": "Гусь кушает.",
    "f_frog.wav": "Лягушка кушает.",
    "f_lion.wav": "Лев кушает.",
    "f_tiger.wav": "Тигр кушает.",
    "f_bee.wav": "Пчела кушает.",
    "f_fox.wav": "Лиса кушает.",
    "f_hedgehog.wav": "Ёжик кушает.",
    "f_hen.wav": "Курица кушает.",
    "f_rooster.wav": "Петушок кушает.",
    "f_donkey.wav": "Ослик кушает.",
    "f_mouse.wav": "Мышка кушает."
}

print(f"Запуск озвучки {len(phrases)} фраз для оптимизированного кормления...")

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

print("✅ Готово! Лишние птицы улетели, голоса записаны.")
