import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Полный список фраз для игры "Кто что ест?"
# По вашей просьбе: на букву У ударения НЕ ставятся (никаких ý), на остальные гласные - ставятся.
phrases = {
    "f_intro.wav": "Угадáй, кто что ест? Покорми́ живóтных!",
    "f_yum.wav": "Ам-ням-ням! Вкусно!",
    "f_win.wav": "Урá! Все живóтные сы́ты!",
    "f_cat.wav": "Кóшка кушает.",
    "f_dog.wav": "Собáка кушает.",
    "f_cow.wav": "Корóва кушает.",
    "f_horse.wav": "Лóшадь кушает.",
    "f_sheep.wav": "Овцá кушает.",
    "f_pig.wav": "Свинья́ кушает.",
    "f_goat.wav": "Козá кушает.",
    "f_wolf.wav": "Волк кушает.",
    "f_goose.wav": "Гусь кушает.",
    "f_frog.wav": "Лягушка кушает.",
    "f_lion.wav": "Лев кушает.",
    "f_tiger.wav": "Тигр кушает.",
    "f_bee.wav": "Пчелá кушает.",
    "f_fox.wav": "Лисá кушает.",
    "f_hedgehog.wav": "Ёжик кушает.",
    "f_hen.wav": "Курица кушает.",
    "f_rooster.wav": "Петушóк кушает.",
    "f_donkey.wav": "Осли́к кушает.",
    "f_mouse.wav": "Мы́шка кушает."
}

print(f"Запуск озвучки {len(phrases)} фраз для мега-кормления...")

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

print("✅ Готово! Все звуковые файлы для новой комнаты успешно сгенерированы.")
